# for loop basic

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print("")


print("__________________")
for i in range(1, 6):
    for j in range(6, i, -1):
        print("*", end="")
    print("")

# print("__________________")
# for i in range(1, 6):
#     for j in range(4, i-1, -1):
#         print(" ", end="")
#     print("*"*i)

print("__________________")
# anotherWay
for i in range(1, 6):
    for j in range(4, i-1, -1):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print("")


print("__________________")

for i in range(1, 6):
    for j in range(i-1):
        print(" ", end="")
    for k in range(6, i, -1):
        print("*", end="")
    print("")
