# Mock data for authentication
mock_users = [
    {"email": "user@example.com", "password": "password123", "id": 1}
]

def authenticate_user(email, password):
    # Simulate user authentication using mock data
    for user in mock_users:
        if user["email"] == email and user["password"] == password:
            return {"access_token": "fake_token", "token_type": "bearer"}
    return None
