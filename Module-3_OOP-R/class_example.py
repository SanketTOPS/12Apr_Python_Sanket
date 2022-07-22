class student:
    stid=12
    stnm='Nirav'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)
    
    def production(self,x,y):
        print("Production:",x*y)

# Object
st=student()
st.getdata()
st.production(34,56)




