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

#prints all contacts and puts them into an array and returns array for use.
def cont_arar():
    cont_array=[]
    open("user_data/contacts","a")
    contacts=open("user_data/contacts","r")
    line=contacts.readline()

    count=0
    while line!="":
        cont_array.append(line[:-1])
        print(str(count+1)+". "+cont_array[count])
        count+=1
        line=contacts.readline()
    contacts.close()
    print("")
    return cont_array
