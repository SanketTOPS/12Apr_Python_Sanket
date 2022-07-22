class student:
    __id=12
    __name="Nirav"

    def getdata(self):
        print("This is getdata")
        print("STudent ID:",self.__id)
        print("Student Name:",self.__name)
    
    def __getsum(self,a,b):
        print("Sum:",a+b)
    
    def answer(self):
        self.__getsum(34,54)

st=student()
st.getdata()
st.answer()