# count = 0
# for i in range(1,5):
#     for j in range(i):
#         count += 1
#         print(count, end="")
#     print("")
#
print("_________________")

for i in range(4):
    num = 1
    for j in range(4-i-1):
        print(" ", end="")
    for k in range(i+1):
        print(num, end=" ")
        num = num * (i-k) // (k+1)
        # print(num)
    print("")

