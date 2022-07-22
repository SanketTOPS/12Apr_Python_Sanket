class g_father:
    gold=0
    house=0

    def g_getdata(self):
        self.gold=input("Enter Gold details:")
        self.house=input("Enter HOuse details:")

class father(g_father):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter Car details:")
        self.bal=input("Enter Bank balance details:")

class son(father):
    def printdata(self):
        print("Gold:",self.gold)
        print("House:",self.house)
        print("Car:",self.car)
        print("Bank Balance:",self.bal)
    
sn=son()
sn.g_getdata()
sn.f_getdata()
sn.printdata()


