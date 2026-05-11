# import numpy as np
#
# arr = np.array([1,2,3,4,5,6,7,8,9])
# print(arr)
#
#
# '''
# types of array
# 1D array #np.array([1,2,3])
# 2D array #np.array([[1,2],[3,4]])
# 3D array #np.array([[[1,2],[3,4]]])
# '''
#
# #methods
#
# print(np.zeros((2,4))) # to create initial matrix in ML
# print(np.ones((2,4)))
# print(np.arange(0,10))
# print(np.linspace(1,10,5))
#
#
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# print(arr.reshape(3,2))
#
# print(arr.ndim)
# print(arr.dtype)
#


#######################################################
import numpy as np
#
# arr = np.array([10,20,30,40])
# print(arr[1])
# print(arr[1:3])

# #2D Indexing
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr[1][2])
# #OR
# print(arr[1,2])
#
# arr = np.array([1,2,3,4])
# print(arr + 2)
#
#
# Aggregation Functions
# arr = np.array([1,2,3,4])
# print(arr.sum()) # sums all element
# print(arr.mean()) # return average
# print(arr.max()) # returns max value
# print(arr.min()) #returns min value
#
# #Random Numbers
# arr = np.array([1,2,3,4])
# print(np.random.rand(3))
# print(np.random.randint(1,10,5)) # create array of random number (min value, max value, number of elements)
#
#
# import numpy as np
#
# marks = np.array([50,60,70,80,90])
#
# print(marks.mean()) # mean, average
# print(marks.std()) # standard deviation



# Intro + why NumPy
# Array creation
# List vs NumPy
# Shape, ndim
# Indexing
# Math operations
# Aggregation
# Random


#Create array of 10 numbers
# Find:
#
# sum
# mean
# max
#reshape into 2x5

# arr = np.array([10,20,30,40,50,60,70,80,90,100])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))
# print(np.reshape(arr,(2,5)))

#Vectorization + Broadcasting + Fast Matrix Operations

#Broadcasting

# import numpy as np
#
# arr = np.array([1, 2, 3])
#
# print(arr + 2)

# import numpy as np
#
# a = np.array([[1,2,3],
#               [4,5,6]])
#
# b = np.array([10,20,30])
# print(a+b)


#Vectorization
# a = [1,2,3]
# b = []
#
# for i in a:
#     b.append(i * 2)
#
# print(b)
#
# import numpy as np
# a = np.array([1,2,3])
# print(a * 2)

#Advanced Indexing
import numpy as np

# arr = np.array([10,20,30,40,50])
# print(arr[arr>25])
# print(arr[[0,2]])

#np.where()
# arr = np.array([10,20,30,40])
# print(np.where(arr > 25,"high","Low"))

# Matrix Multiplication
# a = np.array([[1,2],
#               [3,4]])
#
# b = np.array([[5,6],
#               [7,8]])
#
# print(np.dot(a,b))  #[[(1*5 + 2*7), (1*6 + 2*8)], [(3*5 + 4*7),(3*6 + 4*8)]]

#np.transpose()
# arr = np.array([[1,2,3],
#                 [4,5,6]])
#
# print(arr.T)



#student + marks
#prediction + normalization

# # import numpy as np
# marks = np.array([50, 60, 70, 80, 90])
# print("Original Data:", marks)
#
# mean = np.mean(marks)
# print("Mean:", mean)
#
# #Standard Deviation
# std = np.std(marks)
# print("Std:", std)
#
#
# normalized = (marks - mean) / std  #marks - mean → center data  #/ std → scale data
# print("Normalized:", normalized)
#
#
# #Student Performance Analyzer
# import numpy as np
#
# Step 1: Student marks (Math, Science, English)
# data = np.array([
#     [80, 70, 60],
#     [90, 85, 88],
#     [60, 65, 70],
#     [75, 80, 85]
# ])
# print("Student Data:\n", data)
#
#
# # Step 2: Average per student
# avg = data.mean(axis=1)
# print("Average per student:", avg)
#
#
# # Step 3: Grade assign
# grade = np.where(avg > 75, "Pass", "Fail")
# print("Grades:", grade)
#
#
# # Step 4: Topper find
# topper = np.argmax(avg)
# print("Topper Index:", topper)
# print("Topper Marks:", data[topper])
#
# # Step 5: Subject-wise average
# subject_avg = data.mean(axis=0)
# print("Subject Avg:", subject_avg)


# Avg → performance
# Grade → classification
# Topper → max value
# Subject avg → analysis



#Create dataset of 5 students, 3 subjects

# Find:
#
# avg
# topper
# grade using where
# normalize data

data = np.array([
    [80, 70, 60],
    [90, 85, 88],
    [60, 65, 70],
    [75, 80, 85],
    [10, 70, 20]
])
avg = np.mean(data, axis=1)
print(avg)

topper = np.argmax(avg)
print(topper)
print(np.where(avg > 75, "Pass", "Fail"))

norm = (data - avg.reshape(-1,1)) / np.std(data, axis=1).reshape(-1,1)
print(norm)