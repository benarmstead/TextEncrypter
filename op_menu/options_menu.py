import others.get_array_contacts as get_array_contacts
import others.clear_s as clear_s

import hashlib
import time

#gives users options to manipulate program data
def options():
    clear_s.clr_sc()
    try:
        menu=input('''1. Back to main menu
2. Add User
3. Delete User
4. View user details
5. Verification

: ''')
    except:
        print("Error")
        exit()

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
