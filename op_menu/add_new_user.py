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

import op_menu.options_menu as options_menu

import time
import hashlib

def add_user():
    #takes user name, checks does not exist
    name=str(input("Enter name: "))
    contacts=open("user_data/contacts","r")
    line=contacts.readline()[:-1]
    while line!="":
        if name==line:
            print("Sorry, name already exists.")
            time.sleep(1)
            options_menu.options()
        line=contacts.readline()[:-1]

    #get times for passwords to be hashed
    hashes=str
    while type(hashes)!=int:
        try:
            hashes=int(input("Times for password to be hashed: "))
        except ValueError:
            print("You must enter a number")
            time.sleep(1)

    keys=[]
    hash_keys=[]
    #gets encryption passwords and turns them into keys
    key=1
    key_num=0
    while key!="q":
        key_num+=1
        key=input("Encryption key "+str(key_num)+" (q to exit): ")
        if key=="q":
            break
        keys.append(key.encode())
        print("Hashing key")
        for count in range(int(hashes)):
            key = hashlib.sha512(key.encode()).hexdigest()
        hash_keys.append(key)

    #writes the data to user files
    open("user_data/"+name+"keysbackup","w").write(str(keys))
    open("user_data/contacts","a").write(name+"\n")
    open("user_data/"+name,"w").write(str(hashes)+"\n"+str(hash_keys))
