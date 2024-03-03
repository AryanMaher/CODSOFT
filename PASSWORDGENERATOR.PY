import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets based on desired complexity
    all_characters = lower_case + upper_case + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        # Check if length is valid (greater than zero)
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets based on desired complexity
    all_characters = lower_case + upper_case + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        # Check if length is valid (greater than zero)
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
