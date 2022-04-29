from cryptography.fernet import Fernet

with open("filekey.key", "rb") as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open("globalvars.txt", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_data = fernet.decrypt(encrypted_data)

with open("globalvars.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)