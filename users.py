


VALID_USERS = {
    "admin": "admin123",
    "student": "student123"
}


current_user = None

def login_system():
    global current_user
    print("========================================")
    print("              MiniOS Login")
    print("========================================")
    
    
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
    
    if current_user:
        print(f"Current User: {current_user}")
    else:
        print("No user is currently logged in.")