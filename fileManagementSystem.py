import os

menuList = ["Create File", "Write File", "Read File", "Rename File", "Delete File", "Search Value", "Exit"]


def menu():
    print("Main Menu:")
    for i in range(1, len(menuList)+1):
        print(f"{i}: {menuList[i-1]}")

def create_file(filename):
    try:
        if os.path.exists(filename):
            raise FileExistsError("File Already Exists")
        open(filename, "x")
        return "File Created Successfully"
    except FileExistsError as e:
        return e


def check_file_exists(filename):
    try:
        if os.path.exists(filename):
            return True
        else:
            raise FileNotFoundError("File Not Found")
    except:
        return FileNotFoundError


def write_file(filename, content):
    try:
        if os.path.exists(filename):
            file = open(filename, "w")
            file.write(content)
            file.close()
            return "File written successfully!!"
        else:
            raise FileNotFoundError("File Not Found")
    except FileNotFoundError as e:
        return e

def read_file(filename):
    try:
        if os.path.exists(filename):
            file = open(filename, "r")
            getData = file.read()
            if len(getData) == 0:
                raise ValueError("File is Empty")
            file.close()
            return getData
        else:
            raise FileNotFoundError("File Not Found")
    except (FileNotFoundError, ValueError) as e:
        return e


def rename_file(filename, newname):
    try:
        if os.path.exists(filename):
            os.rename(filename, newname)
            return "File Renamed Successfully"
        else:
            raise FileNotFoundError("Old File Not Found")
    except FileNotFoundError as e:
        return e

def delete_file(filename):
    try:
        if os.path.exists(filename):
            confirm = input("Are you sure you want to delete? (y/n): ")
            if confirm == "y" or confirm == "Y":
                os.remove(filename)
                return "File Deleted Successfully !!"
            elif confirm == "n" or confirm == "N":
                return "File deletion cancelled"
            else:
                raise IOError("Invalid Input")
        else:
            raise FileNotFoundError("File Not Found")
    except Exception as e:
        return e

def search_string(filename, value):
    try:
        if os.path.exists(filename):
            file = open(filename, "r")
            for word in file:
                if value in word:
                    return "Match Found!"
                else:
                    raise ValueError("Match not Found")
            file.close()
        else:
            raise FileNotFoundError("File Not Found")
    except (FileNotFoundError, ValueError) as e:
        return e