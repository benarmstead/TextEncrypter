'''
TextEncrypter - Encrypts text before being sent
Copyright (C) 2020  Ben Armstead

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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
    input("Press enter to continue: ")

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
