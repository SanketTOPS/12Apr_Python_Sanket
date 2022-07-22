import re

#email="sanket2020@gmail.com"
email=input("Enter Email:")

email_pattern=r"\b[a-z0-9._]+@+[a-z]+[.]+[a-z]{2,}$"
#email_pattern=r'^[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}\b'
#email_pattern= r'\b[a-z0-9._]+@[a-z0-9._]+\.[a-z]\b'

x=re.fullmatch(email_pattern,email)
if x:
    print("Email is valid!")
else:
    print("Error...Invalid Email!")