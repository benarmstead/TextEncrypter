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
    
    try:
        menu = input('''1. Encrypt
2. Decrypt
3. Back to main menu

: ''')
    except:
        print("Error")
        exit()


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
