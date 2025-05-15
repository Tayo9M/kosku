import os
import psycopg2
import psycopg2.extras

# Function to get database connection
def get_db_connection():
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
    conn.autocommit = True
    return conn

# Function to escape SQL literals
def escape_sql_string(s):
    if s is None:
        return 'NULL'
    return "'" + str(s).replace("'", "''") + "'"

# Main function to create backup
def create_backup():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Get all tables
    cursor.execute("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)
    tables = [row['table_name'] for row in cursor.fetchall()]
    
    # Create backup file
    with open('backups/kos_management_backup.sql', 'w') as backup_file:
        # Add header
        backup_file.write("-- Database backup created for Sistem Pencatatan Penginapan Kos\n")
        backup_file.write("-- Date: " + str(os.popen('date').read().strip()) + "\n\n")
        
        # First, create schema
        backup_file.write("-- Schema creation\n\n")
        
        # Get and write create table statements
        for table in tables:
            # Get columns
            cursor.execute(f"""
                SELECT column_name, data_type, is_nullable, column_default
                FROM information_schema.columns
                WHERE table_name = '{table}'
                ORDER BY ordinal_position
            """)
            columns = cursor.fetchall()
            
            # Check for primary key
            cursor.execute(f"""
                SELECT c.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name)
                JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
                    AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
                WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = '{table}'
            """)
            primary_keys = [row['column_name'] for row in cursor.fetchall()]
            
            # Check for foreign keys
            cursor.execute(f"""
                SELECT
                    tc.constraint_name,
                    kcu.column_name,
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                    AND tc.table_schema = kcu.table_schema
                JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                    AND ccu.table_schema = tc.table_schema
                WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name='{table}'
            """)
            foreign_keys = cursor.fetchall()
            
            # Generate CREATE TABLE statement
            create_table = f"DROP TABLE IF EXISTS {table} CASCADE;\n"
            create_table += f"CREATE TABLE {table} (\n"
            
            # Add columns
            column_defs = []
            for col in columns:
                col_str = f"    {col['column_name']} {col['data_type']}"
                if col['column_default']:
                    col_str += f" DEFAULT {col['column_default']}"
                if col['is_nullable'] == 'NO':
                    col_str += " NOT NULL"
                column_defs.append(col_str)
            
            # Add primary key
            if primary_keys:
                pk_str = f"    PRIMARY KEY ({', '.join(primary_keys)})"
                column_defs.append(pk_str)
            
            # Add foreign keys
            for fk in foreign_keys:
                fk_str = f"    CONSTRAINT {fk['constraint_name']} FOREIGN KEY ({fk['column_name']}) " + \
                       f"REFERENCES {fk['foreign_table_name']}({fk['foreign_column_name']})"
                column_defs.append(fk_str)
            
            create_table += ",\n".join(column_defs)
            create_table += "\n);\n\n"
            
            backup_file.write(create_table)
        
        # Now, dump data for each table
        backup_file.write("\n-- Table data\n\n")
        
        for table in tables:
            backup_file.write(f"-- Data for table {table}\n")
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            
            if rows:
                column_names = [desc[0] for desc in cursor.description]
                
                for row in rows:
                    values = []
                    for val in row:
                        values.append(escape_sql_string(val))
                    
                    insert_stmt = f"INSERT INTO {table} ({', '.join(column_names)}) VALUES ({', '.join(values)});\n"
                    backup_file.write(insert_stmt)
            
            backup_file.write("\n")
    
    print(f"Backup completed. File saved to 'backups/kos_management_backup.sql'")
    conn.close()

if __name__ == "__main__":
    create_backup()