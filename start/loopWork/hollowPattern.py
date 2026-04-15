for i in range(1, 6):
    for j in range(4, i-1, -1):
        print(" ", end="")
    for k in range(1, i*2):
        if k == 1 or k == i*2-1 or i == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print("")


print("________________")
for i in range(1, 6):
    for j in range(4, i-1, -1):
        print(" ", end="")
    for k in range(1, i*2):
        if k == 1 or k == i*2-1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
for i in range(5, 0, -1):
    for j in range(4, i - 1, -1):
        print(" ", end="")
    for k in range(1, i * 2):
        if k == 1 or k == i * 2 - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")


print("________________")
for i in range(1, 5):
    for j in range(1,5):
        if i == 1 or j == 1 or i == 4 or j == 4:
            print(" *", end="")
        else:
            print("  ", end="")
    print("")