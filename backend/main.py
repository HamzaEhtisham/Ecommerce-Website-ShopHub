import os
from flask import Flask, jsonify, request, session, send_from_directory, render_template
from flask_cors import CORS
from database import (init_database, create_user, get_all_users, get_user_by_id, 
                     update_user, delete_user, authenticate_admin, get_all_admins, 
                     create_admin, update_admin_password, create_product, get_all_products,
                     get_product_by_id, update_product, delete_product)

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'your_secret_key_here_change_in_production'  # For session management
CORS(app, supports_credentials=True)  # Enable CORS with credentials support

# Initialize database on startup
init_database()

# User routes
@app.route('/')
def index():
    return render_template('index.html')

# Serve static JS, CSS, media files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Catch-all route to support React Router
@app.route('/<path:path>')
def fallback(path):
    static_path = os.path.join(app.static_folder, path)
    if os.path.exists(static_path):
        return send_from_directory(app.static_folder, path)
    return render_template("index.html")





# User routes
@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users"""
    try:
        users = get_all_users()
        # Convert sqlite3.Row objects to dictionaries
        users_list = [dict(user) for user in users]
        return jsonify({"success": True, "users": users_list})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID"""
    try:
        user = get_user_by_id(user_id)
        if user:
            return jsonify({"success": True, "user": dict(user)})
        else:
            return jsonify({"success": False, "error": "User not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/users', methods=['POST'])
def add_user():
    """Create a new user"""
    try:
        data = request.get_json()
        
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"success": False, "error": "Name and email are required"}), 400
        
        name = data['name'].strip()
        email = data['email'].strip()
        
        # Basic email validation
        if '@' not in email or '.' not in email:
            return jsonify({"success": False, "error": "Invalid email format"}), 400
        
        create_user(name, email)
        return jsonify({"success": True, "message": "User created successfully"}), 201
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    """Update an existing user"""
    try:
        data = request.get_json()
        
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"success": False, "error": "Name and email are required"}), 400
        
        name = data['name'].strip()
        email = data['email'].strip()
        
        # Basic email validation
        if '@' not in email or '.' not in email:
            return jsonify({"success": False, "error": "Invalid email format"}), 400
        
        rows_affected = update_user(user_id, name, email)
        
        if rows_affected > 0:
            return jsonify({"success": True, "message": "User updated successfully"})
        else:
            return jsonify({"success": False, "error": "User not found"}), 404
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    """Delete a user"""
    try:
        rows_affected = delete_user(user_id)
        
        if rows_affected > 0:
            return jsonify({"success": True, "message": "User deleted successfully"})
        else:
            return jsonify({"success": False, "error": "User not found"}), 404
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Admin routes
@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    """Admin login endpoint"""
    try:
        data = request.get_json()
        
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"success": False, "error": "Username and password are required"}), 400
        
        username = data['username'].strip()
        password = data['password']
        
        admin = authenticate_admin(username, password)
        
        if admin:
            session['admin_id'] = admin['id']
            session['admin_username'] = admin['username']
            return jsonify({
                "success": True, 
                "message": "Login successful",
                "admin": {
                    "id": admin['id'],
                    "username": admin['username'],
                    "email": admin.get('email', '')
                }
            })
        else:
            return jsonify({"success": False, "error": "Invalid credentials"}), 401
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/admin/logout', methods=['POST'])
def admin_logout():
    """Admin logout endpoint"""
    session.pop('admin_id', None)
    session.pop('admin_username', None)
    return jsonify({"success": True, "message": "Logged out successfully"})

@app.route('/api/admin/check', methods=['GET'])
def check_admin_session():
    """Check if admin is logged in"""
    if 'admin_id' in session:
        return jsonify({
            "success": True, 
            "logged_in": True,
            "admin": {
                "id": session['admin_id'],
                "username": session['admin_username']
            }
        })
    else:
        return jsonify({"success": True, "logged_in": False})

@app.route('/api/admin/admins', methods=['GET'])
def get_admins():
    """Get all admins (admin only)"""
    try:
        if 'admin_id' not in session:
            return jsonify({"success": False, "error": "Unauthorized"}), 401
        
        admins = get_all_admins()
        admins_list = [dict(admin) for admin in admins]
        return jsonify({"success": True, "admins": admins_list})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Product routes
@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all products (public endpoint)"""
    try:
        products = get_all_products()
        products_list = [dict(product) for product in products]
        return jsonify({"success": True, "products": products_list})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a specific product by ID (public endpoint)"""
    try:
        product = get_product_by_id(product_id)
        if product:
            return jsonify({"success": True, "product": dict(product)})
        else:
            return jsonify({"success": False, "error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/admin/products', methods=['POST'])
def add_product():
    """Create a new product (admin only)"""
    try:
        if 'admin_id' not in session:
            return jsonify({"success": False, "error": "Unauthorized"}), 401
            
        data = request.get_json()
        
        if not data or 'name' not in data or 'price' not in data:
            return jsonify({"success": False, "error": "Name and price are required"}), 400
        
        name = data['name'].strip()
        
        try:
            price = float(data['price'])
            if price < 0:
                return jsonify({"success": False, "error": "Price cannot be negative"}), 400
        except (ValueError, TypeError):
            return jsonify({"success": False, "error": "Invalid price format"}), 400
        
        description = data.get('description', '').strip()
        
        create_product(name, price, description)
        return jsonify({"success": True, "message": "Product created successfully"}), 201
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/admin/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    """Update an existing product (admin only)"""
    try:
        if 'admin_id' not in session:
            return jsonify({"success": False, "error": "Unauthorized"}), 401
            
        data = request.get_json()
        
        if not data or 'name' not in data or 'price' not in data:
            return jsonify({"success": False, "error": "Name and price are required"}), 400
        
        name = data['name'].strip()
        
        try:
            price = float(data['price'])
            if price < 0:
                return jsonify({"success": False, "error": "Price cannot be negative"}), 400
        except (ValueError, TypeError):
            return jsonify({"success": False, "error": "Invalid price format"}), 400
        
        description = data.get('description', '').strip()
        
        rows_affected = update_product(product_id, name, price, description)
        
        if rows_affected > 0:
            return jsonify({"success": True, "message": "Product updated successfully"})
        else:
            return jsonify({"success": False, "error": "Product not found"}), 404
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/admin/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    """Delete a product (admin only)"""
    try:
        if 'admin_id' not in session:
            return jsonify({"success": False, "error": "Unauthorized"}), 401
            
        rows_affected = delete_product(product_id)
        
        if rows_affected > 0:
            return jsonify({"success": True, "message": "Product deleted successfully"})
        else:
            return jsonify({"success": False, "error": "Product not found"}), 404
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"success": False, "error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"success": False, "error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)