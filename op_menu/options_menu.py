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

#gives users options to manipulate program data
def options():
    clear_s.clr_sc()
    menu=input('''1. Back to main menu
2. Add User
3. Delete User
4. View user details
5. Verification

: ''')
    try:

        if menu=="1":
            return 0
        elif menu=="2":
            clear_s.clr_sc()
            import op_menu.add_new_user as add_new_user
            add_new_user.add_user()
        elif menu=="3":
            clear_s.clr_sc()
            import op_menu.delete_the_user as delete_the_user
            delete_the_user.delete_user()
        elif menu=="4":
            clear_s.clr_sc()
            import op_menu.view_the_user as view_the_user
            view_the_user.view_user()
        elif menu=="5":
            clear_s.clr_sc()
            import op_menu.verify_user as verify_user
            verify_user.verification()
        else:
            print("Please enter a number from 1-5!!!")
            time.sleep(1)
    except ValueError:
        print("You must enter a number!!!")
        time.sleep(1)
