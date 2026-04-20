import csv

with open("data.csv", "w", newline="") as csvFile:
    columns = ['name', 'age', 'city']
    writers = csv.DictWriter(csvFile, fieldnames=columns)
    writers.writeheader()

    writers.writerows([{'name': 'parth', 'age': 26, 'city': 'ahm'}, {'name': 'parth2', 'age': 26, 'city': 'ahm'}])
