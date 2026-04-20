import csv

# with open('data.csv') as csvFile:
#     reader = csv.reader(csvFile)
#
#     for i in reader:
#         for index in range(len(i)):
#             print(f"\t{i[index]}", end=" ")
#         print()

# with open('data.csv') as csvFile:
#     reader = csv.DictReader(csvFile)
#     linenum = 0
#     for i in reader:
#         if linenum == 0:
#             print(f'\t{" ".join(i)}')
#             linenum += 1
#         print(f"\t{i['name']} {i['age']} {i['city']}")


with open('data.csv') as csvFile:
    reader = csv.DictReader(csvFile)
    linenum = 0
    for i in reader:
        if linenum == 0:
            print(f'\t{" ".join(i)}')
            linenum += 1
        print(f"{i['name']} {i['age']} {i['city']}")