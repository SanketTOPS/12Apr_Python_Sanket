mydict={}

n=int(input("HOw many pairs you want to store?:"))

for i in range(n):
    key=input("Enter you key:")
    value=input("Enter your value:")
    mydict[key]=value

print(mydict)