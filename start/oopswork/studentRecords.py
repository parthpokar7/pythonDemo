import csv

class University:
    column = []
    filename = ''
    def __init__(self):
        self.filename = input("enter filename: ")


    def create_record(self):
        self.column = input("enter column name (comma separated): ").split(',')
        with open(f"{self.filename}.csv", "w", newline="") as record:
            writer = csv.DictWriter(record, fieldnames=self.column)
            writer.writeheader()


class Students(University):

    def __init__(self):
        super().__init__()

    def add_student(self):
        with open(f"{self.filename}.csv", "a+", newline="") as file:
            file.seek(0)
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            print(headers)

            data = []
            for i in headers:
                data.append(input(f"Enter Value for {i}: "))

            file.seek(0, 2)
            writers = csv.writer(file)
            writers.writerow(data)

    def view_allStudents(self):
        with open(f"{self.filename}.csv", 'r') as records:
            reader = csv.DictReader(records)
            linenum = 0
            for i in reader:
                if linenum == 0:
                    print(f'\t{" ".join(i)}')
                    linenum += 1
                print(f"\t{i['name']} {i['enrollment']} {i['course']}")

    def update_record(self):
        search_column = input("enter column name you want to search in: ")

        with open(f"{self.filename}.csv", 'r+') as records:
            reader = csv.DictReader(records)
            headers = reader.fieldnames
            rows = list(reader)
            # print(headers)
            found = False

            if search_column in headers:
                search_data = input("enter search keyword:")
                for row in rows:
                    if row[search_column] == search_data:
                        found = True
                        for i in headers:
                            print(f"Current {i}: {row[i]}")
                            row[i] = (input(f"Enter Value for {i}: "))

                with open(f"{self.filename}.csv", 'w', newline='') as records:
                    writer = csv.DictWriter(records, fieldnames=headers)
                    writer.writeheader()
                    writer.writerows(rows)

                if not found:
                    print("match not found !!")
            else:
                print("column not available in the file")




std = Students()
# std.create_record()
# std.add_student()
# std.view_allStudents()
std.update_record()