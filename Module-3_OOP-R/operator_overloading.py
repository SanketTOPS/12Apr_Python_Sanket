class student:

    # Operator Overloading
    def getdata(self,a,b):
        print("Sum:",a+b)
    
    def userdata(self,fnm,lnm):
        print("Fullname:",fnm+lnm)


st=student()
st.getdata(23,45)
st.userdata("Sanket","Chauhan")