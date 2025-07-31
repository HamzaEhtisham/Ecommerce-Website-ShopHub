import sqlite3
import os

DATABASE_PATH = 'database.db'

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

def init_database():
    """Initialize database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Products table (example)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Admin table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert default admin if not exists
    cursor.execute('SELECT COUNT(*) FROM admins')
    admin_count = cursor.fetchone()[0]
    if admin_count == 0:
        cursor.execute('''
            INSERT INTO admins (username, password, email) 
            VALUES (?, ?, ?)
        ''', ('admin', 'admin123', 'admin@project.com'))
    
    conn.commit()
    conn.close()

def execute_query(query, params=(), fetch=False):
    """Execute a query and return results if needed"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query, params)
        
        if fetch:
            if fetch == 'all':
                result = cursor.fetchall()
            elif fetch == 'one':
                result = cursor.fetchone()
            else:
                result = cursor.fetchmany(fetch)
        else:
            result = cursor.rowcount
            
        conn.commit()
        return result
    
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def create_user(name, email):
    """Create a new user"""
    query = "INSERT INTO users (name, email) VALUES (?, ?)"
    return execute_query(query, (name, email))

def get_all_users():
    """Get all users"""
    query = "SELECT * FROM users ORDER BY created_at DESC"
    return execute_query(query, fetch='all')

def get_user_by_id(user_id):
    """Get user by ID"""
    query = "SELECT * FROM users WHERE id = ?"
    return execute_query(query, (user_id,), fetch='one')

def update_user(user_id, name, email):
    """Update user"""
    query = "UPDATE users SET name = ?, email = ? WHERE id = ?"
    return execute_query(query, (name, email, user_id))

def delete_user(user_id):
    """Delete user"""
    query = "DELETE FROM users WHERE id = ?"
    return execute_query(query, (user_id,))

# Admin functions
def authenticate_admin(username, password):
    """Authenticate admin login"""
    query = "SELECT * FROM admins WHERE username = ? AND password = ?"
    return execute_query(query, (username, password), fetch='one')

def get_all_admins():
    """Get all admins"""
    query = "SELECT id, username, email, created_at FROM admins ORDER BY created_at DESC"
    return execute_query(query, fetch='all')

def create_admin(username, password, email):
    """Create a new admin"""
    query = "INSERT INTO admins (username, password, email) VALUES (?, ?, ?)"
    return execute_query(query, (username, password, email))

def update_admin_password(admin_id, new_password):
    """Update admin password"""
    query = "UPDATE admins SET password = ? WHERE id = ?"
    return execute_query(query, (new_password, admin_id))

# Product functions
def create_product(name, price, description):
    """Create a new product"""
    query = "INSERT INTO products (name, price, description) VALUES (?, ?, ?)"
    return execute_query(query, (name, price, description))

def get_all_products():
    """Get all products"""
    query = "SELECT * FROM products ORDER BY created_at DESC"
    return execute_query(query, fetch='all')

def get_product_by_id(product_id):
    """Get product by ID"""
    query = "SELECT * FROM products WHERE id = ?"
    return execute_query(query, (product_id,), fetch='one')

def update_product(product_id, name, price, description):
    """Update product"""
    query = "UPDATE products SET name = ?, price = ?, description = ? WHERE id = ?"
    return execute_query(query, (name, price, description, product_id))

def delete_product(product_id):
    """Delete product"""
    query = "DELETE FROM products WHERE id = ?"
    return execute_query(query, (product_id,))
