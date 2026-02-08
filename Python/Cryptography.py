'''
DAY 16: Cryptography
Today I Learned about cryptography in Python, which protects sesitive information by encoding it
For that we have 2 files, one is the vault that contains the encrypted information, and the other is the key that contains the key to decrypt the information
To encrypt the information, we can use the Fernet class from the cryptography library, which provides symmetric encryption:
'''

from cryptography.fernet import Fernet
import os

class PasswordVault:
    def __init__(self):
        self.key_file = "master.key"
        self.key = self.load_or_generate_key()
        self.cipher = Fernet(self.key)

    def load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            return key
        
    def encrypt_data(self, plainText):
        return self.cipher.encrypt(plainText.encode())
    
    def decrypt_data(self, txtBytes):
        return self.cipher.decrypt(txtBytes).decode()
    
vault = PasswordVault()
secret = "This is a secret message!"
encrypted = vault.encrypt_data(secret)
print("Encrypted:", encrypted)
decrypted = vault.decrypt_data(encrypted)
print("Decrypted:", decrypted)


'''
Security is crucial when handling sensitive information, encrypting is one of the ways to protect these datas!
'''