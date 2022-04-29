from cryptography.fernet import Fernet

with open("filekey.key", "rb") as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open("globalvars.txt", "rb") as file:
    cleartext = file.read()

encrypted_data = fernet.encrypt(cleartext)

with open("globalvars.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)