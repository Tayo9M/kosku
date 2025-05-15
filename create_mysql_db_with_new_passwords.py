import os
import psycopg2
import psycopg2.extras
import datetime
from werkzeug.security import generate_password_hash

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

def generate_mysql_with_new_passwords():
    """Generate SQL file with compatible password hashes for MySQL."""
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
    with open('mysql_data_with_new_passwords.sql', 'w') as sql_file:
        # Add header
        sql_file.write("-- MySQL Compatible Insert Statements with updated password hashes\n")
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
            
            if table == 'users':
                # Khusus untuk tabel users, buat password hash yang kompatibel
                cursor.execute("SELECT * FROM users")
                rows = cursor.fetchall()
                for row in rows:
                    columns = [desc[0] for desc in cursor.description]
                    values = []
                    
                    for i, val in enumerate(row):
                        if columns[i] == 'password_hash':
                            # Buat password default: [username]123
                            default_password = f"{row['username']}123"
                            # Generate password hash yang kompatibel
                            hash_value = generate_password_hash(default_password, method='pbkdf2:sha256')
                            values.append(f"'{hash_value}'")
                        else:
                            values.append(escape_sql_string(val))
                    
                    insert_stmt = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(values)});\n"
                    sql_file.write(insert_stmt)
            else:
                # Untuk tabel lain, lakukan seperti biasa
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
        
        # Add password information
        sql_file.write("\n-- Default password untuk semua pengguna: [username]123\n")
        sql_file.write("-- Contoh: admin123, manager1123, staff1123, viewer1123, dll.\n")
    
    # Generate password information file
    with open('new_passwords.txt', 'w') as info_file:
        info_file.write("DEFAULT PASSWORDS FOR ALL USERS:\n\n")
        
        cursor.execute("SELECT username, role FROM users ORDER BY role")
        users = cursor.fetchall()
        
        for user in users:
            info_file.write(f"Username: {user['username']}\n")
            info_file.write(f"Role: {user['role']}\n")
            info_file.write(f"Password: {user['username']}123\n\n")
    
    conn.close()
    print("MySQL compatible SQL with new password hashes generated in 'mysql_data_with_new_passwords.sql'")
    print("Password information saved in 'new_passwords.txt'")

if __name__ == "__main__":
    generate_mysql_with_new_passwords()