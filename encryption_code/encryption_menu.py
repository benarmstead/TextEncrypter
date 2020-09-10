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

import encryption_code.encryption as encryption
import encryption_code.decryption as decryption
import others.clear_s as clear_s

import time

#offers menu whether to encrypt or decrypt
#also saves encryption keys into string 
def crypt(name):
    clear_s.clr_sc()
    file=open("user_data/"+name,"r")
    no_hashes=file.readline()
    key=eval(file.readline())
    keys=[]
    for x in range(len(key)):
        keys.append(key[x].encode())

    menu = input('''1. Encrypt
2. Decrypt
3. Back to main menu

: ''')
    if menu == "1":
        clear_s.clr_sc()
        encryption.encrypt_start(keys,name)
        print("encrypted")
        time.sleep(0.3)
    elif menu == "2":
        clear_s.clr_sc()
        decryption.decrypt_last(keys,name)
    elif menu == "3":
        return 0
    else:
        print("You must enter a number from 1-3!!!")
        time.sleep(1)
