# users.py

# A dictionary acting as our simulated user database
VALID_USERS = {
    "admin": "admin123",
    "student": "student123"
}

# Variable to track who is currently logged in
current_user = None

def login_system():
    global current_user
    print("========================================")
    print("              MiniOS Login")
    print("========================================")
    
    # Keep asking until a valid login is provided
    while current_user is None:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if username in VALID_USERS and VALID_USERS[username] == password:
            print("\nLogin successful.")
            print(f"\nWelcome, {username}!\n")
            current_user = username
        else:
            print("\nError: Invalid username or password. Please try again.\n")

def whoami():
    # Feature requirement: Print the current user
    if current_user:
        print(f"Current User: {current_user}")
    else:
        print("No user is currently logged in.")