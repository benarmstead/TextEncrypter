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
