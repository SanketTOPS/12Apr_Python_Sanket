class student:
    def userlogin(self,username,password):
        print("Username:",username)
        print("Password:",password)

class otherstudent(student):
    def userlogin(self, username, password):
        return super().userlogin(username, password)


ot=otherstudent()
ot.userlogin("tops","tops?123")
