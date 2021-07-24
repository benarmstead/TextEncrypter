#imports clipboard manipulation
import pyperclip

#imports cryptography librarys
import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

#decrypts the last sent message, then copys data in clipboard for decryption, then decrypts message
def decrypt_last(keys,name):
    last = decrypt_start(keys,(open("user_data/"+name+"lm.enc","r").readline()).encode())
    print("The data in your clipboard is used for decryption.")
    data = (pyperclip.paste()).encode()
    print("Last message: "+last+"\n")
    print(decrypt_start(keys,data))
    try:
        input("Press enter to continue: ")
    except:
        print("Error")
        exit()
#decrypts the message with the appropriate keys
def decrypt_start(keys,data):
    count=len(keys)
    while count!=0:
        try:#trys, therefore allowing for incorrect cipher text to be entered and not crash the program
            data = decrypt_function(keys[count-1],data)#decrypts the data with the current key
            count-=1
        except:
            return ("Cannot Decrypt\n\n")
    return (data.decode())#returns decrypted data

#function that acutally does the decryption
def decrypt_function(key, source, decode = True):
    key = SHA256.new(key).digest()
    source = base64.b64decode(source)
    IV = source[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])
    padding = data[-1]
    return data[:-padding]
