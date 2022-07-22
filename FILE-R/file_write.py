fl=open("stdata.txt","a")

#fl.write("This is Python.")


stid=input("Enter ID:")
stnm=input("Enter Name:")
stcity=input("Enter City:")

fl.write(f"\nStID:{stid}\nStname:{stnm}\nStCity:{stcity}")
