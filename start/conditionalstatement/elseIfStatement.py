a = int(input("Enter your age: "))
if a>0 and a<=5:
    print("you are a baby")
elif a>5 and a <=10:
    print("you are a kid")
elif a>10 and a<=17:
    print("you are teenage")
elif a>17 and a<=35:
    print("you are adult")
elif a>35 and a<=59:
    print("you are matured")
elif a>59 and a<=100:
    print("you are senior citizen")
else:
    print("enter valid age")
