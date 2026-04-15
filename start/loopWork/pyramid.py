'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

#Full Pyramid
for i in range(1, 6):
    for j in range(4, i-1, -1):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print("")

print("_______________")
#inverted Full Pyramid
for i in range(1, 6):
    for j in range(i-1):
        print(" ", end="")
    for k in range(6, i, -1):
        print("* ", end="")
    print("")

print("_______________")
#diamond
for i in range(1, 6):
    for j in range(4, i-1, -1):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print("")
for i in range(1, 5):
    for j in range(i):
        print(" ", end="")
    for k in range(5, i, -1):
        print("* ", end="")
    print("")

print("_______________")
#hourGlass
for i in range(1, 6):
    for j in range(i-1):
        print(" ", end="")
    for k in range(6, i, -1):
        print("* ", end="")
    print("")
for i in range(2, 6):
    for j in range(4, i-1, -1):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print("")
print("_______________")
