s1=int(input("Enter Subject1 Mark:"))
s2=int(input("Enter Subject2 Mark:"))
s3=int(input("Enter Subject3 Mark:"))


if s1>=40 and s2>=40 and s3>=40: #Root
    total=s1+s2+s3
    print("Total:",total)
    print("------------------")

    pr=total/3
    print("PR:",pr)
    print("------------------")

    if pr>=70:
        print("Result:Dist.")
    elif pr>=60:
        print("Result:First Class")
    elif pr>=50:
        print("Result:Second Class")
    elif pr>=40:
        print("Result:Pass Class")

else:
    print("Result:Fail")