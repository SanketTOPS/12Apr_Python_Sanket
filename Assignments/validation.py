import re

username=input("Enter Username:")
password=input("Enter Password:")
firstname=input("Enter Firstname:")
lastname=input("Enter Lastname:")

u_ptrn="[A-Z@!#$%._]+[a-z@!#$%._]+[0-9@!#$%._]+[@!#$%._]"
p_ptrn="[A-Z@!#$%._]+[a-z@!#$%._]+[0-9@!#$%._]+[@!#$%._]"
f_ptrn="^[A-Za-z]"
l_ptrn="^[A-Za-z]"


u_check=re.findall(u_ptrn,username)
p_check=re.findall(p_ptrn,password)
f_check=re.findall(f_ptrn,firstname)
l_check=re.findall(l_ptrn,lastname)

if u_check and p_check and f_check and l_check:
    fl=open("signup.txt","a")
    fl.write("---------User--------\n")
    fl.write(f"{username}\n")
    fl.write(f"{password}\n")
    fl.write(f"{firstname}\n")
    fl.write(f"{lastname}\n")
else:
    print("Error....Somthing went wrong, Try again!")