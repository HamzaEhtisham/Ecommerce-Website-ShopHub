# 🔐 Admin Credentials

## Default Admin Login

When you start the application for the first time, a default admin account is automatically created:

### 📋 Credentials:
- **Username**: `admin`
- **Password**: `admin123`
- **Email**: `admin@admin.com`

## 🚀 How to Login

### Using API:
```bash
curl -X POST http://localhost:5000/api/admin/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

### Using Postman or Frontend:
**Endpoint**: `POST /api/admin/login`
**Body (JSON)**:
```json
{
  "username": "admin",
  "password": "admin123"
}
```

## 🔧 Admin API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/admin/login` | Admin login |
| POST | `/api/admin/logout` | Admin logout |
| GET | `/api/admin/check` | Check if admin is logged in |
| GET | `/api/admin/admins` | Get all admins (requires login) |

## 🛡️ Security Notes

⚠️ **IMPORTANT**: Change the default password in production!

1. The default admin credentials are only for development
2. In production, create secure passwords
3. Consider implementing password hashing (bcrypt)
4. Change the session secret key in `main.py`

## 🔄 Change Password

To change admin password, you can directly update in database or create an API endpoint:

```sql
UPDATE admins SET password = 'new_password' WHERE username = 'admin';
```

## 📊 Database Table Structure

```sql
CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
