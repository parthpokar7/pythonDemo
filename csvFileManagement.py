import os
import csv

menuList = ["Create File", "Write File", "Read File", "Rename File", "Delete File", "Exit"]
def menu():
    print("Main Menu:")
    for i in range(1, len(menuList)+1):
        print(f"{i}: {menuList[i-1]}")

def check_file_exists(filename):
    try:
        if os.path.exists(filename):
            return True
        else:
            raise FileNotFoundError("File Not Found")
    except FileNotFoundError as e:
        return e

def create_file(filename):
    try:
        if check_file_exists(filename) == True:
            raise FileExistsError("File Already Exists")
        else:
            header = colums = input("enter column names (comma separated): ")
            with open(filename, "w", newline="") as csvFile:
                writers = csv.DictWriter(csvFile, fieldnames=header.split(","))
                writers.writeheader()
            return "File Created Successfully"
    except FileExistsError as e:
        return e


def write_data(filename):
    try:
        if check_file_exists(filename) == True:
            with open(filename, "a+", newline="") as file:
                file.seek(0)
                reader = csv.DictReader(file)
                headers = reader.fieldnames

                data = []
                for i in headers:
                    data.append(input(f"Enter Value for {i}: "))

                file.seek(0, 2)
                writers = csv.writer(file)
                writers.writerow(data)

                choice = input("do you want to add another data? (y/n): ")

                if choice.lower() == 'y':
                    write_data(filename)
            return "File Updated Successfully !!"
        else:
            raise FileNotFoundError("File Do Not Exists")
    except FileNotFoundError as e:
        return e


def read_data(filename):
    try:
        if check_file_exists(filename) == True:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for i in reader:
                    for index in range(len(i)):
                        print(f"\t{i[index]}", end=" ")
                    print()

        else:
            raise FileNotFoundError("File Do Not Exists")
    except FileNotFoundError as e:
        return e

def rename_file(filename):
    try:
        if os.path.exists(filename):
            newname = input("enter new file name: ")
            os.rename(filename, f"{newname}.csv")
            return "File Renamed Successfully"
        else:
            raise FileNotFoundError("Old File Not Found")
    except FileNotFoundError as e:
        return e


def delete_file(filename):
    try:
        if os.path.exists(filename):
            confirm = input("Are you sure you want to delete? (y/n): ")
            if confirm.lower() == "y":
                os.remove(filename)
                return "File Deleted Successfully !!"
            elif confirm.lower() == "n":
                return "File deletion cancelled"
            else:
                raise IOError("Invalid Input")
        else:
            raise FileNotFoundError("File Not Found")
    except Exception as e:
        return e
