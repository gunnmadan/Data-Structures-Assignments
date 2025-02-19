import hashlib

password_hash_table = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(username, password):
    if username in password_hash_table:
        return f"Error: Username '{username}' is already taken."
    password_hash_table[username] = hash_password(password)
    return f"Password saved for user '{username}'."

def compare_password(username, password):
    if username not in password_hash_table:
        return f"Error: Username '{username}' not found."
    return password_hash_table[username] == hash_password(password)

# Sample function calls and expected outputs
print(save_password("user1", "mypassword123"))  
print(save_password("user1", "newpassword456"))  
print(save_password("user2", "securepassword4567"))  

print(compare_password("user1", "mypassword123"))  
print(compare_password("user1", "wrongpassword"))  
print(compare_password("user3", "any_password"))   
