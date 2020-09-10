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

import others.clear_s as clear_s
import others.get_array_contacts as get_array_contacts

import time
import os

def home():
    #displays home menu
    clear_s.clr_sc()
    print("##########HOME##########")
    print("Enter the number of the item to select.")
    cont_array=list(get_array_contacts.cont_arar())
    print('''    (o) for options
    (m) for manual
    (e) for exit''')


    main_menu = str(input("\n: "))
    try:
        if main_menu=="e":
            clear_s.clr_sc()
            exit()
        if main_menu=="o":
            import op_menu.options_menu as options_menu
            options_menu.options()

        if main_menu=="m":
            clear_s.clr_sc()
            #prints the manual
            print(open("others/manual.txt","r").read())
            input("Press enter to continue: ")

        elif int(main_menu)<=len(cont_array):

            import encryption_code.encryption_menu as encryption_menu
            encryption_menu.crypt(cont_array[int(main_menu)-1])

        else:
            print("Please enter a number within range")
            time.sleep(1)

    except ValueError:
        print("ValueError")

#checks if dependancies are installed, if not, installs them

if not os.path.exists("user_data"):
    os.makedirs("user_data")
open("user_data/first_launch.txt","a")
file=open("user_data/first_launch.txt","r")
if file.readline()=="":
    os.system("pip3 install pyperclip")
    os.system("pip3 install pycryptodome")
    open("user_data/first_launch.txt","w").write("1")

else:
    a=1
while 1:
    home()
