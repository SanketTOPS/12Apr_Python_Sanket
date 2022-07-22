class student:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

# Object
"""st=student()
st.getdata()
st.stid=34
st.stnm='Nirav'
st.getdata()"""

# Instance
student().getdata()
student().stid=78
student().stnm='Meet'
student().getdata()
