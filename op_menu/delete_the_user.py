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
