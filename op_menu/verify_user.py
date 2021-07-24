import others.get_array_contacts as get_array_contacts
import others.clear_s as clear_s

import hashlib
import time
import pyperclip



def verification():
    #gets user to be verified and hashes to be performed
    cont_array=list(get_array_contacts.cont_arar())
    try:
        name=int(input("Enter the user you wish to verify: "))
        hashes=input("Enter the amount of hashes you wish to perform: ")
        lines=str(open("user_data/"+cont_array[int(name-1)],"r").readlines())
    except:
        print("This must be a number and within range!")
        time.sleep(1)
        return 0

    clear_s.clr_sc()
    #calculates hash of their config and then prints and copys to clipboard
    print("Hashing config ...")
    count=0
    while int(count)<=int(hashes):
        lines = hashlib.sha512(lines.encode()).hexdigest()
        count+=1
    clear_s.clr_sc()

    print("The result of the config is: \n"+str(lines))
    print("Coppied hash to clipboard")
    pyperclip.copy(lines)
    
    #checks hash is the same as their friends
    check=str(input("Enter your friends result to see if they match (enter to skip): "))
    if str(check)==str(lines):
        clear_s.clr_sc()
        print("CORRECT MATCH")
        time.sleep(1.5)
    else:
        clear_s.clr_sc()
        print("INCORRECT MATCH")
        time.sleep(1.5)
