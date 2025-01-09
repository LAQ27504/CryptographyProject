import base64
import secrets
import qrcode
import qrcode.console_scripts
from PIL import Image

def generate_and_show_qr(data: str):
    """
    Generates a QR code for the given data and displays it as a popup.

    Args:
        data (str): The data to encode in the QR code.
    """
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is small, 40 is large)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4)
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    qr_image.save("qr.png")

    # Display the QR code
    qr_image.show()

def generate_secret_key(key_length:int = 32):
    """
    Generates a secret key based on the number of bytes suitable for length of the key 
    Args:
        base (int): The length of key
    """
    num_bytes = 8
    num_bits = 5
    num_bytes = ( key_length // num_bytes ) * num_bits
    random_bytes = secrets.token_bytes(num_bytes)
    return base64.b32encode(random_bytes).decode('utf-8')

# Generate url base on the information
def generate_url(secret : str, label : str, issuer : str = None):
    issuer_str = ""
    if issuer:
        issuer_str = f"&issuer={issuer}"
    url = f'otpauth://totp/{label}?secret={secret}{issuer_str}'
    return url
