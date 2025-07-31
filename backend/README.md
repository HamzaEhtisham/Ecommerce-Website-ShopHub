# Python Backend with SQLite Database

This is a simple Flask backend API that uses SQLite database without SQLAlchemy for data storage.

## Features

- **Flask Web Framework**: Lightweight and flexible Python web framework
- **SQLite Database**: Native SQLite integration without ORM
- **CORS Support**: Cross-Origin Resource Sharing enabled for frontend integration
- **RESTful API**: Standard REST endpoints for CRUD operations
- **User Management**: Complete user management system with CRUD operations

## Project Structure

```
backend/
├── main.py          # Main Flask application
├── database.py      # Database utility functions
├── app.py          # Basic Flask app (alternative version)
├── test_api.py     # API testing script
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## Setup Instructions

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

3. **Server will start on**: `http://localhost:5000`

## API Endpoints

### Base URL: `http://localhost:5000/api`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/api/users` | Get all users |
| GET | `/api/users/<id>` | Get user by ID |
| POST | `/api/users` | Create new user |
| PUT | `/api/users/<id>` | Update user |
| DELETE | `/api/users/<id>` | Delete user |
| GET | `/api/products` | Get all products |
| GET | `/api/products/<id>` | Get product by ID |
| POST | `/api/admin/products` | Create new product (admin only) |
| PUT | `/api/admin/products/<id>` | Update product (admin only) |
| DELETE | `/api/admin/products/<id>` | Delete product (admin only) |
| POST | `/api/admin/login` | Admin login |
| POST | `/api/admin/logout` | Admin logout |
| GET | `/api/admin/check` | Check admin session |

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Products Table (Example)
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Usage Examples

### Create User
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Get All Users
```bash
curl http://localhost:5000/api/users
```

### Update User
```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.updated@example.com"}'
```

### Delete User
```bash
curl -X DELETE http://localhost:5000/api/users/1
```

## Testing

Run the test script to test all API endpoints:
```bash
python test_api.py
```

## Database File

- The SQLite database file `database.db` will be created automatically in the backend directory when you first run the application.
- No SQLAlchemy is used - pure SQLite3 Python module for database operations.

## Key Features

1. **Pure SQLite**: Uses Python's built-in `sqlite3` module
2. **No ORM**: Direct SQL queries for better performance and control
3. **Error Handling**: Proper error handling and response formatting
4. **CORS Enabled**: Ready for frontend integration
5. **Parameterized Queries**: Protection against SQL injection
6. **Connection Management**: Proper database connection handling
