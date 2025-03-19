import random
import string

def password_generator(length):
    # Check if length is valid
    if length <= 0:
        raise ValueError("Password length must be greater than zero.")
    
    # Define character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = "".join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        # Ask user for password length
        user_len = int(input("Enter password length: "))
        
        # Generate and display password
        password = password_generator(user_len)
        print(f"Generated password: {password}")
        
        # Exit loop after successful generation
        break
    except ValueError as e:
        # Handle errors (e.g., invalid input)
        print(f"Error: {e}. Please enter a valid number.")