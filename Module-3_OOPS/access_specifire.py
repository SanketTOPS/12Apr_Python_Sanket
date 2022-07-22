class student:
    __stid=12
    __stnm="Sanket"

    def getsum(self,a,b):
        print("Sum:",a+b)
    
    def getdata(self):
        print("Student ID:",self.__stid)
        print("Student Name:",self.__stnm)

st=student()
st.getsum(23,43)
st.getdata()