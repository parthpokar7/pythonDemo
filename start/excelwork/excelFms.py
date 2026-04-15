import excelFileManagement as efms

efms.menu()
choice = int(input("select action from above Menu: "))

while choice != 6:
    if choice == 1:
        filename = input("Enter File Name: ")
        headers = input("Enter Column Titles (Comma seperated): ")
        print(efms.create_file(f"{filename}.xlsx", headers.split(",")), "\n")
    elif choice == 2:
        filename = input("Enter File Name: ")
        checkFile = efms.check_file_exists(f"{filename}.xlsx")
        if checkFile == True:
            print(efms.write_data(f"{filename}.xlsx"))
        else:
            print(checkFile)
    elif choice == 3:
        filename = input("Enter File Name: ")
        checkFile = efms.check_file_exists(f"{filename}.xlsx")
        if checkFile == True:
            efms.read_data(f"{filename}.xlsx")
        else:
            print(checkFile)
    elif choice == 4:
        name = input("enter existing file name: ")
        newname = input("enter new file name: ")
        print(efms.rename_file(f"{name}.txt", f"{newname}.txt"), "\n")
    elif choice == 5:
        name = input("enter existing file name: ")
        print(efms.delete_file(f"{name}.txt"), "\n")
    else:
        print("Invalid Selection!\n")

    efms.menu()
    choice = int(input("select action from above Menu: "))
