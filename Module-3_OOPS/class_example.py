class student:
    stid=12
    stnm="Sanket"

    def getdata(self):
        print("This is Student Class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)
    
    def getmul(self):
        x=34
        y=89
        #print("Mul:",x*y)
        return x*y

    
# Object of class
st=student()
print(st.stid)
print(st.stnm)
st.getdata()
st.getsum(23,55)
print(st.getmul())