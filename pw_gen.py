import random
import string

def generate_password(length=16):
    # 1. Define the "pool" of characters
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # 2. Use a loop to pick random characters from the pool
    # This is a "List Comprehension" - a very pro Python move
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password

# --- The User Interface ---
print("--- PROFESSIONAL PASSWORD GENERATOR ---")

try:
    user_length = int(input("Enter desired password length (e.g., 12): "))
    
    if user_length < 8:
        print("Warning: Security experts recommend at least 8 characters!")
    
    new_password = generate_password(user_length)
    
    print("-" * 30)
    print(f"YOUR NEW PASSWORD: {new_password}")
    print("-" * 30)
    print("Keep it secret. Keep it safe.")

except ValueError:
    print("Error: Please enter a number for the length.")