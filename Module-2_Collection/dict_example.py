mydict={"id":101,"name":"sanket","city":"rajkot"}
print(mydict)
#print(mydict["name"])
#print(mydict.get("city"))

#print(len(mydict))

"""if 'sub' in mydict:
    print("YEs...")
else:
    print("Nooo")"""

#print(mydict.keys())
#print(mydict.values())
#print(mydict.items())

"""for i in mydict:
    print(i)"""

"""for i in mydict.values():
    print(i)"""

"""for i in mydict.items():
    print(i)"""

#mydict["id"]=102


mydict["sub"]="Python"
mydict.pop("name")
#del mydict
#print(mydict)

newdict=mydict.copy()
print(newdict)

