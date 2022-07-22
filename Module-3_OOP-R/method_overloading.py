class student:

    # Method Overloading
    def getdata(self,a,b):
        print("Sum:",a+b)
    
    def getdata(self,id,name):
        print("Student ID:",id)
        print("Student Name:",name)

st=student()
st.getdata(12,'Sanket')


