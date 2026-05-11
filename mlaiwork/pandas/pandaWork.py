'''
Pandas = Data handle karne ka king tool
Excel jaisa data Python me handle karna
Tables (rows + columns) me kaam karna
Data clean, filter, analyze karna


Sales report
Website users data


Pandas kyu use hota hai?
CSV, Excel read/write
Data cleaning (missing values)
Filtering
Grouping (analysis)
ML ke liye data prepare

#Core Concept
1 Series (1D)  #Single column data
2 DataFrame (2D)  #Table (rows + columns)

'''
import pandas as pd

# data=[1,2,3,4]
# s=pd.Series(data)
# print(s)


#DataFrame
data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Marks": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}
df= pd.DataFrame(data)
# print(df)


#Data Read
# df = pd.read_csv("data.csv")
# print(df["Name"])

# df = pd.read_excel("data.xlsx")
# print(df["HEX"])
#
# #Data Check
# print(df.head()) #returns first 5 index
# print(df.tail()) #returns last 5 index

# print(df.info())
# print(df.describe())

#Column Access
# print(df["Name"])
# print(df[["Name", "HEX"]])

#Row Access
# print(df.loc[0])
# print(df.iloc[0])

#Filtering
# print(df[df["Marks"]>80])

#New Column Add

# df["Result"] = ["Pass", "Pass", "Fail"]
# print(df)

#Drop Column
# df.drop("Result", axis=1, inplace=True)

#Missing Values

# df = pd.read_csv("missing_data.csv")
df = pd.read_excel("missing_data.xlsx")


print(df.isnull()) #returns True if value is missing
print("___________________________")
print(df.dropna()) #it skips the raw where value is missing
print("___________________________")
print(df.fillna(0)) #replaces with 0 where the value is missing

#Sorting
print("___________________________")
print("___________________________")

print(df.sort_values("Name"))
