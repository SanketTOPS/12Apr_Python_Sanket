class student:
    stid=0
    stnm=''

    def getdata(self):
        self.stid=input("Enter ID:")
        self.stnm=input("Enter Name:")
    
    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

st=student()

for i in range(4):
    st.getdata()
    st.printdata()

#for i in range(4):
   
