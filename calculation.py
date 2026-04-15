def add(a,b,c):
    if c == 1:
        return "sum : ", a+b
    elif c == 2:
        return "substraction : ",  a-b
    elif c == 3:
        return "product : ", a*b
    elif c == 4:
        return "division : ", a/b
    else:
        return "invalid Operation!!"