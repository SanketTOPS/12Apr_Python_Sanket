try:
    a=int(input("Enter value of A:"))
    b=int(input("Enter value of B:"))
except Exception as e:
    print(e)
finally:
    x=int(input("Enter value of X:"))
    y=int(input("Enter value of Y:"))
    print("Production:",x*y)
