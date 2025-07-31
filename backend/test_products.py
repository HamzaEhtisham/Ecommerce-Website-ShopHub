import requests
import json

BASE_URL = "http://localhost:5000/api"

def test_product_apis():
    print("Testing Product APIs...\n")
    
    # First, login as admin
    print("1. Admin Login:")
    login_data = {
        "username": "admin",
        "password": "admin123"
    }
    
    session = requests.Session()  # Use session to maintain cookies
    response = session.post(f"{BASE_URL}/admin/login", json=login_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    if response.status_code != 200:
        print("Login failed! Cannot proceed with product tests.")
        return
    
    # Test 2: Get all products (initially empty)
    print("2. Getting all products:")
    response = session.get(f"{BASE_URL}/products")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 3: Create a new product
    print("3. Creating a new product:")
    product_data = {
        "name": "Laptop",
        "price": 50000.99,
        "description": "High-performance gaming laptop"
    }
    response = session.post(f"{BASE_URL}/admin/products", json=product_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 4: Create another product
    print("4. Creating another product:")
    product_data2 = {
        "name": "Mobile Phone",
        "price": 25000.00,
        "description": "Latest smartphone with 5G"
    }
    response = session.post(f"{BASE_URL}/admin/products", json=product_data2)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 5: Get all products after creation
    print("5. Getting all products after creation:")
    response = session.get(f"{BASE_URL}/products")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 6: Get specific product
    print("6. Getting product with ID 1:")
    response = session.get(f"{BASE_URL}/products/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 7: Update product
    print("7. Updating product with ID 1:")
    update_data = {
        "name": "Gaming Laptop Pro",
        "price": 75000.99,
        "description": "Updated high-performance gaming laptop with RTX graphics"
    }
    response = session.put(f"{BASE_URL}/admin/products/1", json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 8: Get updated product
    print("8. Getting updated product:")
    response = session.get(f"{BASE_URL}/products/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 9: Try to create product without login (should fail)
    print("9. Testing unauthorized product creation:")
    new_session = requests.Session()  # New session without login
    product_data3 = {
        "name": "Unauthorized Product",
        "price": 1000.00,
        "description": "This should fail"
    }
    response = new_session.post(f"{BASE_URL}/admin/products", json=product_data3)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

if __name__ == "__main__":
    try:
        test_product_apis()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running on http://localhost:5000")
