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
