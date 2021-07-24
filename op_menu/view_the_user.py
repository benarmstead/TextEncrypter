import others.get_array_contacts as get_array_contacts
import others.clear_s as clear_s

import time

#function to view details of a user
def view_user():
    cont_array=list(get_array_contacts.cont_arar())

    try:
        name=int(input("Enter the number of the user you wish to view: "))
        name=cont_array[name-1]

    except:
        print("This must be a number and within range!")
        time.sleep(1)
        return 0

    clear_s.clr_sc()
    file=open("user_data/"+name,"r")
    hash1=file.readline()

    print("Name: "+name)
    print("Hashes per password: "+hash1[:-1])
    print("Keys: ")

    keys=eval(file.readline())
    for x in range (len(keys)):
        print(keys[x])

    print("\nOriginal passwords\n")
    old_pass=eval(open("user_data/"+name+"keysbackup","r").readline())
    for c in range (len(old_pass)):
        print(old_pass[c].decode())
    input("\n\nPress enter to continue: ")
