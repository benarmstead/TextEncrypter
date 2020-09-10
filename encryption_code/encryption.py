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

#imports clipboard manipulation and time
import pyperclip
import time

#imports cryptography librarys
import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

#takes the keys and user name and encrypts the data, aswell as storing it (as the last message) in name+lm.enc
#also copies cipher text to clipboard
def encrypt_start(keys,name):
    data = input("Encrypt: ")
    for count in range(len(keys)):
        data = encrypt_function(keys[count],data.encode())
    file = open("user_data/"+str(name)+"lm.enc","w").write(str(data))
    print(data)
    pyperclip.copy(data);print("Copied to clipboard")
    time.sleep(1)

#function that encrypts the data
def encrypt_function(key,source, encode = True):
    key = SHA256.new(key).digest()#turns into a 256bit key rather than 512bit key so it can be used in AES
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    data = IV + encryptor.encrypt(source)
    return base64.b64encode(data).decode("latin-1")
