# Applying HMAC in authenticator app
## Description
This is our small python project for simulate the server/client workflow of authenticator app for cryptography subject. 
This simulation work based on TOTP - Time-based One-Time Password
which have server and client side, which server representing for providing secret key from the services and client representing for generate 6 digits otp from the users
## Instruction
***THIS INSTRUCTION ARE RUNNING IN TERMINAL***
### Initialize
Create a venv for this project in python in terminal  
**Note:** Please create venv in this repo for easy following
```
python -m venv <your venv name>
```
Then activate it:
- Window:
```
.\<your venv name>\Scripts\activate.bat
```
- Linux/MacOs:
```
source ./<your venv name>/bin/activate
```
After that, you can install the requires libraries in requirements.txt
```
pip install -r ./requirement.txt
```
However, to running pyzbar, we need some other installation. 

![screenshot of pyzbar installation.](/assets/pyzbar_installation.png)

### How to run the scripts
Run python **runsys.py** in terminal
```
python runsys.py
```
It will show us 2 options

![screenshot of runsys entry.](/assets/runsys_entry.png)

If you want to create a new secret key, type ***open server***, this will pop up a new terminal for letting you working on server side.   
It will ask you to fill some info then generate a new qr code in the root folder   
*Example*

![screenshot of qr exmaple.](/assets/example1.png)

After generating qr code, the server will asking if you want to check if your token with server's secret key is valid token or not. If you press **y** or **yes**, it will jump to next "page" for entering your token.

![screenshot of the server exmaple](/assets/server_example.png)

At this, you can go back to the terminal that run the **runsys.py** scripts, and enter **open client**. Again, it will pop up another terminal again and it will show the generate of 6 digits code of the previous generate key from the servers


![screenshot of client exmaple](/assets/client_example.png)

And you can enter the code shown in the client to the server and it will print Valid Token.

![screenshot of output exmaple](/assets/output_example.png)

And the otp code will re-generate for each 30 seconds. That is all about how to operate our simple project

## Overall
This project help us learn more about how HMAC with SHA-1 is applied in TOTP or Authenticator app. And hope that you can understand :3333

## Member:
**Leader**: [LAQ27504](https://github.com/LAQ27504)