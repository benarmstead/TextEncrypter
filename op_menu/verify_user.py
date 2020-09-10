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
