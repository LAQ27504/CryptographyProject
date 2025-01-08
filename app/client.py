from pyzbar.pyzbar import decode
from PIL import Image
from urllib.parse import unquote, urlparse, parse_qs
from TOTP.secretToDigits import generate_totp_tokens
import os
import time
import pyotp

def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux/Unix
        os.system('clear')


def generate_otp(secret_key):
    valid_token = generate_totp_tokens(secret_key)
    print(f"This is out 6 digits token: {valid_token}")
    print("---------")
    py_totp = pyotp.TOTP(secret_key)
    print(f"This is pyotp library 6 digits token: {py_totp.now()}")
    print("---------")

def extract_url_from_qr(image_path):
    image = Image.open(image_path)

    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            data = obj.data.decode("utf-8") 
            print(f"Decoded URL/Data: {data}")
            return data
    else:
        print("No QR code found in the image.")
        return None


def get_url_params(url):
    parsed_url = urlparse(url)
    
    page = unquote(parsed_url.path.lstrip('/'))

    query_params = parse_qs(parsed_url.query)
    query_params["page"] = [page]

    return query_params

def main():
    image_path = "qr.png"
    url = extract_url_from_qr(image_path)
    params = get_url_params(url=url)
    secret = params.get("secret", [None])[0]  
    issuer = params.get("issuer", [None])[0]  
    page = params.get("page", [None])[0]

    last_second = None  
    
    clear_terminal()
    print("=============================================")
    generate_otp(secret)
    print(f"Service: {issuer}")
    print(f"Code id: {page}")
    print("=============================================")

    while True:
        current_time = time.localtime()
        current_seconds = current_time.tm_sec 
        
        if current_seconds == 0 or current_seconds == 30:
            if current_seconds != last_second:
                clear_terminal()
                print("=============================================")
                generate_otp(secret)
                print(f"Service: {issuer}")
                print(f"Code id: {page}")
                print("=============================================")
                last_second = current_seconds  
        time.sleep(1)

if __name__ == "__main__":
    main()