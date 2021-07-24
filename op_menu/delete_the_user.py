import others.get_array_contacts as get_array_contacts

import os
import time

#deletes a selected user
def delete_user():
    cont_array=list(get_array_contacts.cont_arar())
    try:
        name=int(input("Enter the number of the user you wish to delete: "))
        name=cont_array[name-1]
    except:
        print("This must be a number and within range!")
        time.sleep(1)
        return 0
    lines=open("user_data/contacts", "r").readlines()
    file=open("user_data/contacts", "w")
    for line in lines:
        if line.strip("\n") != name:
            file.write(line)
    file.close()

    try:
        os.remove("user_data/"+name)
        os.remove("user_data/"+name+"keysbackup")
        os.remove("user_data/"+name+"lm.enc")
    except FileNotFoundError:
        a=1
    print("User deleted")
