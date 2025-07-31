import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:5000/api"

def test_api():
    print("Testing Backend API...\n")
    
    # Test 1: Get all users (initially empty)
    print("1. Getting all users:")
    response = requests.get(f"{BASE_URL}/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 2: Create a new user
    print("2. Creating a new user:")
    user_data = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 3: Create another user
    print("3. Creating another user:")
    user_data2 = {
        "name": "Jane Smith",
        "email": "jane@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=user_data2)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 4: Get all users again
    print("4. Getting all users after creation:")
    response = requests.get(f"{BASE_URL}/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 5: Get specific user
    print("5. Getting user with ID 1:")
    response = requests.get(f"{BASE_URL}/users/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 6: Update user
    print("6. Updating user with ID 1:")
    update_data = {
        "name": "John Updated",
        "email": "john.updated@example.com"
    }
    response = requests.put(f"{BASE_URL}/users/1", json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running on http://localhost:5000")
