# marks = int(input("enter marks: "))
#
# try:
#     if marks < 0 or marks > 100:
#         raise ValueError
#     elif marks >= 40:
#         print("pass")
#     else:
#         print("failed")
#
# except Exception:
#     print("marks should be in range of 0 to 100")


# username = "admin"
# password = "1234"
#
# try:
#     uName = input("enter username: ")
#     uPass = input("enter password: ")
#     if username != uName:
#         raise NameError("Incorrect Username")
#     if password != uPass:
#         raise PermissionError("Incorrect Password ")
#     # if username == "admin" and password == "1234":
#     #     print("Login Successful")
# except (NameError, PermissionError) as e:
#     print(e)
# else:
#     print("Login Successful")


# bal = 5000
# try:
#     amount = int(input("enter amount: "))
#     if amount > bal:
#         raise ValueError("Insufficient Balance")
#
#     if amount <= 0:
#         raise ValueError("Enter Valid Amount !!")
# except ValueError as e:
#     print(e)
# else:
#     print("withdrawal successful")
