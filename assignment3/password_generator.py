import random
import string

def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_characters = lower + upper + digits + special
    
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random characters from the combined set
    if length > 4:
        password += random.choices(all_characters, k=length-4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired length for your password (minimum length 4): "))
            if length < 4:
                print("Password length should be at least 4 characters.")
            else:
                password = generate_password(length)
                print(f"Generated password: {password}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        another = input("Do you want to generate another password? (yes/no): ")
        if another.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
