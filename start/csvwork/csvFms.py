import csvFileManagement as cfms

cfms.menu()
choice = int(input("select action from above Menu: "))

while choice != 6:
    if choice == 1:
        filename = input("enter file name: ")
        print(cfms.create_file(f"{filename}.csv"), "\n")
    elif choice == 2:
        filename = input("enter file name: ")
        print(cfms.write_data(f"{filename}.csv"), "\n")
    elif choice == 3:
        filename = input("enter file name: ")
        cfms.read_data(f"{filename}.csv")
        print("\n")
    elif choice == 4:
        name = input("enter existing file name: ")
        print(cfms.rename_file(f"{name}.csv"), "\n")
    elif choice == 5:
        name = input("enter existing file name: ")
        print(cfms.delete_file(f"{name}.csv"), "\n")
    else:
        print("Invalid Selection!\n")

    cfms.menu()
    choice = int(input("select action from above Menu: "))
