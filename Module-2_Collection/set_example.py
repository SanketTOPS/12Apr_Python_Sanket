import MySQLdb


myset={'A','B','C','D','E'}
print(myset)
#print(myset[0])

#print(len(myset))

"""if 'X' in myset:
    print("Yes..")
else:
    print("Nooo")"""

#myset.add("F")
#myset.update(["G","H","I","B","D"])
#myset.remove("X")
#myset.discard("F")
#myset.pop()
#del myset
#print(myset)


newset={"P","Q","R","S","A","B","C"}

#x=myset.union(newset)
x=myset.intersection(newset)
print(x)
