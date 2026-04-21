# flatten nested List
myList = [[1,2], [3,4], [5,6]]
newList = [j for i in myList for j in i]
print(newList)


# condition replacement
myList = [1,2,3,4,5,6,7,8,9]
newList = ['Fizz' if i%3==0 else i for i in myList]
print(newList)


# cartesian product
list1 = [1,2]
list2 = ['A', 'B']
myList = [(i,j) for i in list1 for j in list2]
print(myList)


# reverse each string in list
list1 = ["cat", "dog", "bird"]
myList = [i[::-1] for i in list1]
print(myList)


# find common from list
list1 = [1,2,3,4]
list2 = [3,4,5,6]
myList = [i for i in list1 for j in list2 if i == j]
print(myList)


# filter palindrome
list1 = ["madam", "python", "level", "world", "civic"]
mylist = [i for i in list1 if i == i[::-1]]
print(mylist)


# count vowels
list1 = ["apple", "banana", "cherry"]
myList = [sum(1 for j in i if j in "aeiou") for i in list1]
print(myList)


# convert to upperCase
list1 = ["hello", "world", "python"]
myList = [i.upper() for i in list1]
print(myList)


# remove empty strings
list1 = ["apple", "", "banana", "", "cherry"]
myList = [i for i in list1 if i]
print(myList)


# find length
list1 = ["data", "science", "AI"]
myList = [len(i) for i in list1]
print(myList)


# square only odd
list1 = [1,2,3,4,5]
myList = [i**2 for i in list1 if i%2 != 0]
print(myList)


# replace negative number with 0
list1 = [2, -3, 4, -1, 0]
myList = [0 if i < 0 else i for i in list1]
print(myList)


# extract first character
list1 = ["apple", "banana", "cherry"]
myList = [i[0] for i in list1]
print(myList)


# generate multiple of 5
myList = [5*i for i in range(1, 100) if 5*i<=50]
print(myList)


# filter words longer than 4 char
list1 = ["pen", "notebook", "book", "laptop"]
myList = [i for i in list1 if len(i) > 4]
print(myList)


# convert int to string
list1 = [1,2,3,4]
myList = [str(i) for i in list1]
print(myList)


# find number divisible by 2 and 3
list1 = [1,2,3,4,6,9,12]
mylist = [i for i in list1 if (i%2==0 and i%3==0)]
print(mylist)