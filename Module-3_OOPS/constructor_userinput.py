class student:

    def __init__(self):
        self.stid=input("Enter ID:")
        self.stnm=input("Enter Name:")
    
    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)


st=student()
st.getdata()