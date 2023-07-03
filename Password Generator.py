import random
import string
import os

funny_password_names = ["funnyjuve", "ezhacka", "wonderful", "amaszing", "dancefloor", "june", "applestree", "ayeaye", "yahoopassword"]



amount = int(input("How Many Passwords Do You Want?: "))

def generate_random_password():
    addon_fun = random.choice(funny_password_names)
    password = addon_fun
    characters = string.ascii_lowercase + string.digits
    spec_characters = ["$", "§", "&", "@", "?", "!", ")", "["]
    for _ in range(4):
        spec_char = random.choice(spec_characters)
        password += spec_char
        password += random.choice(characters)
    for _ in range(4):
        spec_char = random.choice(spec_characters)
        password += spec_char
        password += random.choice(characters)
    return password

count = 0
passwords = []
for _ in range(amount):
    count += 1
    random_password = generate_random_password()
    passwords.append(random_password)
    colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']
    reset_color = '\033[0m'
    random_color = random.choice(colors)
    print(random_color + str(count) + "- " + random_password + reset_color)

save_secret = input("Do you want to save one as a secret (y/n)? ")
if save_secret.lower() == 'y':
    secret_count = 0
    while True:
        secret_count += 1
        secret_number = input("Which one (number)? ")
        if secret_number.isdigit() and 0 < int(secret_number) <= len(passwords):
            secret_name = f"secret-name-{secret_count}"
            os.environ[secret_name] = passwords[int(secret_number) - 1]
            print(f"Password {secret_number} saved as secret: {secret_name}")
            break
        else:
            print("Invalid number!")
          
access_password = input("Do you want to access your password (y/n)? ")
if access_password.lower() == 'y':
    while True:
        secret_number = input("Which password (number)? ")
        if secret_number.isdigit() and 0 < int(secret_number) <= len(passwords):
            print(f"Password {secret_number}: {passwords[int(secret_number) - 1]}")
            break
        else:
            print("Invalid number!")


print("All passwords saved and generated successfully.")
