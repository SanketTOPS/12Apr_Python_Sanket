import re

#username="Sanket2020"

username=input("Enter Username:")

unm_pattren="[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattren,username)

if x:
    print("Username Valid!")
else:
    print("Error...Invalid Username.")
