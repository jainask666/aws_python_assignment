per=float(input("Enter a percentage"))
if  per>=60:
    print("First class")
elif per>=50 and per<60:
    print("Second class")
elif per>=40 and per<50:
    print("Pass class")
else:
    print("Fail")
