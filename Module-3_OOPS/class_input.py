class student:
    stid=12
    stnm='Nirav'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

    def getsum(self,a,b):
        print("Sum:",a+b)

st=student()
st.getdata()

x=int(input("Enter A:"))
y=int(input("Enter B:"))
st.getsum(x,y)


