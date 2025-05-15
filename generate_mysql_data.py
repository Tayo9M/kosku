import os
import psycopg2
import psycopg2.extras
import datetime

def get_db_connection():
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
    conn.autocommit = True
    return conn

def escape_sql_string(s):
    if s is None:
        return 'NULL'
    elif isinstance(s, bool):
        return '1' if s else '0'
    elif isinstance(s, (int, float)):
        return str(s)
    elif isinstance(s, datetime.datetime):
        return f"'{s.strftime('%Y-%m-%d %H:%M:%S')}'"
    elif isinstance(s, datetime.date):
        return f"'{s.strftime('%Y-%m-%d')}'"
    else:
        return "'" + str(s).replace("'", "''") + "'"

def generate_mysql_insert_queries():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Get all tables
    cursor.execute("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)
    tables = [row['table_name'] for row in cursor.fetchall()]
    
    # Order tables correctly to handle foreign key constraints
    table_order = []
    # Tables without foreign keys first
    priority_tables = ['users', 'properties']
    
    for table in priority_tables:
        if table in tables:
            table_order.append(table)
            tables.remove(table)
    
    # Add remaining tables
    table_order.extend(tables)
    
    # Create SQL file with MySQL compatible inserts
    with open('mysql_data_inserts.sql', 'w') as sql_file:
        # Add header
        sql_file.write("-- MySQL Compatible Insert Statements for Sistem Pencatatan Penginapan Kos\n")
        sql_file.write("-- Generated: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n\n")
        
        # Disable foreign key checks at the beginning
        sql_file.write("SET FOREIGN_KEY_CHECKS=0;\n\n")
        
        # Create TRUNCATE statements to clear existing data
        sql_file.write("-- TRUNCATE statements to clear existing data\n")
        for table in reversed(table_order):
            sql_file.write(f"TRUNCATE TABLE {table};\n")
        sql_file.write("\n")
        
        # Now, generate insert statements for each table
        for table in table_order:
            sql_file.write(f"-- Data for table {table}\n")
            
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            
            if rows:
                column_names = [desc[0] for desc in cursor.description]
                
                for row in rows:
                    values = []
                    for val in row:
                        values.append(escape_sql_string(val))
                    
                    insert_stmt = f"INSERT INTO {table} ({', '.join(column_names)}) VALUES ({', '.join(values)});\n"
                    sql_file.write(insert_stmt)
            
            sql_file.write("\n")
        
        # Re-enable foreign key checks at the end
        sql_file.write("SET FOREIGN_KEY_CHECKS=1;\n")
    
    # Create view file with table data for inspection
    with open('mysql_data_display.txt', 'w') as display_file:
        display_file.write("-- Table Data Summary --\n\n")
        
        for table in table_order:
            display_file.write(f"=== {table} ===\n")
            
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            
            if rows:
                column_names = [desc[0] for desc in cursor.description]
                display_file.write(" | ".join(column_names) + "\n")
                display_file.write("-" * (sum(len(name) for name in column_names) + 3 * (len(column_names) - 1)) + "\n")
                
                # Show a few rows (up to 10) for review
                for i, row in enumerate(rows):
                    if i >= 10:
                        display_file.write(f"... {len(rows) - 10} more rows\n")
                        break
                    row_values = []
                    for val in row:
                        if val is None:
                            row_values.append("NULL")
                        elif isinstance(val, (datetime.datetime, datetime.date)):
                            row_values.append(val.strftime('%Y-%m-%d'))
                        else:
                            row_values.append(str(val))
                    display_file.write(" | ".join(row_values) + "\n")
            else:
                display_file.write("(No data)\n")
            
            display_file.write("\n")
    
    conn.close()
    print("MySQL compatible insert statements generated in 'mysql_data_inserts.sql'")
    print("Data summary for review saved in 'mysql_data_display.txt'")

if __name__ == "__main__":
    generate_mysql_insert_queries()