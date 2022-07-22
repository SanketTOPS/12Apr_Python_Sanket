def getdata(data):
    dt=[]
    for i in data:
        ln=len(i)
        #print(f"{i} = {ln}")
        dt.append((len(i),i))
    dt.sort()
    print(dt[-1])
        
ls=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    el=input("Enter list element:")
    ls.append(el)

getdata(ls)