from TOTP.generateKey import *
from TOTP.secretToDigits import generate_totp_tokens
import pyotp
import time
import os 

def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux/Unix
        os.system('clear')

def generate_otp(secret_key):
    valid_token = generate_totp_tokens(secret_key)
    return valid_token

def main():
    print("This is server side.")
    email = input("Register device: ")
    issuer = "Group 4"
    email = email.replace(" ", "%20")
    issuer = issuer.replace(" ", "%20")
    print(f"Generating secret code of {issuer}")
    secret_key = generate_secret_key(64)
    print(f"Secret key is: {secret_key}")
    secret_url = generate_url(secret=secret_key, label=email, issuer=issuer)
    print(f"Generate url: {secret_url}")
    generate_and_show_qr(secret_url)

    while True:
        print("Are you ready to test the otp ?? ")
        choice = input("Yes[y]/No[n]: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            clear_terminal()
            while True:
                user_token = input("Enter the 6 digits code here: ")
                valid_token = generate_otp(secret_key)
                if user_token == valid_token:
                    print("Valid token")
                else:
                    print("Invalid token !!!! Try again")
                print("======================")

        else:
            print("Take time :>>")
if __name__ == "__main__":
    main()