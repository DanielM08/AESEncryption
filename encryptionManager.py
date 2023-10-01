from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class EncryptionManager:
  def __init__(self):
    self.initializationVector = 'Gl/5thWPPhbD7+T9t31wIg==' # valor default para o vetor de inicialização

  def encrypts(self, message, secret_key):
    data = str.encode(message) # Transforma string em bytes
    key = str.encode(secret_key) # Transforma string em bytes
    iv = b64decode(self.initializationVector)

    cipher = AES.new(key, AES.MODE_CBC, iv) # Referência: https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode 

    cipherTextBytes = cipher.encrypt(pad(data, AES.block_size))

    iv = b64encode(cipher.iv).decode('utf-8')
    cipherText = b64encode(cipherTextBytes).decode('utf-8')    

    return cipherText

  def decrypts(self, encodedCipherText, secret_key):        
    key = str.encode(secret_key) # Transforma string em bytes
    iv = b64decode(self.initializationVector)
    
    cipherText = b64decode(encodedCipherText)

    cipher = AES.new(key, AES.MODE_CBC, iv) # Referência: https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
    message = unpad(cipher.decrypt(cipherText), AES.block_size)

    return message