import fileManagementSystem as fms

fms.menu()
choice = int(input("select action from above Menu: "))


while choice != 7:
    if choice == 1:
        filename = input("enter file name: ")
        print(fms.create_file(f"{filename}.txt"), "\n")
    elif choice == 2:
        name = input("enter file name: ")
        content = input("write content to write file: ")
        print(fms.write_file(f"{name}.txt", content), "\n")
    elif choice == 3:
        name = input("enter file name: ")
        print(fms.read_file(f"{name}.txt"), "\n")
    elif choice == 4:
        name = input("enter existing file name: ")
        newname = input("enter new file name: ")
        print(fms.rename_file(f"{name}.txt", f"{newname}.txt"), "\n")
    elif choice == 5:
        name = input("enter existing file name: ")
        print(fms.delete_file(f"{name}.txt"), "\n")
    elif choice == 6:
        name = input("enter file name: ")
        value = input("enter search keyword: ")
        print(fms.search_string(f"{name}.txt", value))
    else:
        print("Invalid Selection!\n")

    fms.menu()
    choice = int(input("select action from above Menu: "))




