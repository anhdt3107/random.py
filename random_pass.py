import string
import random

def generate_password(length):
    # Generate a list of all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    #convert 'characters' string to list
    characters = list(characters)
    random.shuffle(characters)

    # Use the random module to shuffle the list of characters
    random.shuffle(characters)

    # Select the specified number of characters from the shuffled list
    password = ''.join(characters[:length])

    return password

# Ask the user for the desired password length
length = int(input("Enter the desired password length: "))

# Generate and print the password
password = generate_password(length)
print("Your new password is:", password)
