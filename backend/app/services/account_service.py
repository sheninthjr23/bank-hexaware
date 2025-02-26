# Simulated in-memory account data
mock_accounts = []

def create_account(account_data: dict):
    # Simulate account creation by appending to the mock "database"
    new_account = {"id": len(mock_accounts) + 1, **account_data}
    mock_accounts.append(new_account)
    return new_account

def get_account(account_id: int):
    # Simulate fetching account by ID
    for account in mock_accounts:
        if account["id"] == account_id:
            return account
    return None

def update_account(account_id: int, account_data: dict):
    # Simulate updating account by ID
    for account in mock_accounts:
        if account["id"] == account_id:
            account.update(account_data)
            return account
    return None

def delete_account(account_id: int):
    # Simulate deleting an account by ID
    for account in mock_accounts:
        if account["id"] == account_id:
            mock_accounts.remove(account)
            return {"message": "Account deleted successfully"}
    return {"message": "Account not found"}
