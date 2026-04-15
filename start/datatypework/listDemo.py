list = [10, 20 , 30 , "parth", 40.50]



print(list + list) #prints two times
print(list[2:])#prints values starting from index 2

print(list[:3]) #print values till index 3 (index 3 is excluded)
print(list[3:300]) #will display values starting index 3 to the last available index upto 300


list.append("5000 as A String") #add new item in the list at the end
print(list)

list.remove(40.50) #removes specific item matching exact value
print(list)

list.append("item to remove")
print(list)

list.pop() #removes item from the last index
print(list)

list.pop(2) #removes item from specified index
print(list)