# a = lambda x:x+10
#
# print(a(20))
#
# myFunc = lambda x, y, z: x + y + z
# print(myFunc(10,20, 30))


#### lamda fuction excersize

# #square of a number
# sq = lambda a: a**2
# print(sq(3))


# #check even or odd
# is_even = lambda a:"even" if a%2 == 0 else "odd"
# print(is_even(3))

# #find max from 2 num
# find_max = lambda a,b: f"{a} is max" if a>b else f"{b} is max"
# print(find_max(20,7))

# #length of string:
# lenOfString = lambda data: len(data)
# print(lenOfString("helloPArth"))
#


# #multiply 2 num
# product = lambda a,b: a*b
# print(product(2,3))

# #reverse a string
# strrev = lambda mystring: mystring[::-1]
# print(strrev("parth"))

# #last char a string
# lastCh = lambda mystring: mystring[-1]
# print(lastCh("parth"))

# #check + - or 0
# num = lambda num : "positive" if num > 0 else ("negative" if num < 0 else "zero")
# print(num(10))

# #celcius to fahrenheit
# c_to_f = lambda c: c*9/5+32
# print(c_to_f(5))

#sum of digits
sumOfDigits = lambda x: sum(x)
print(sumOfDigits([1, 2, 3]))

