'''day of week using number'''
# day = int(input("enter number between 1 to 7: "))
# match day:
#     case 1:
#         print("sunday")
#     case 2:
#         print("monday")
#     case 3:
#         print("tuesday")
#     case 4:
#         print("wednesday")
#     case 5:
#         print("thursday")
#     case 6:
#         print("friday")
#     case 7:
#         print("saturday")
#     case _:
#         print("Holy Christ, you are living on jupiter !!")


'''simple calculator using operator'''
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# operator = input("select operation (+,-,*,/): ")
#
# match operator:
#     case "+":
#         print(num1 + num2)
#     case "-":
#         print(num1 - num2)
#     case "*":
#         print(num1 * num2)
#     case "/":
#         print(num1 / num2)
#     case _:
#         print("invalid operation")


'''vowel or consonent checker'''
# ch = input("enter character: ").lower()
# if len(ch) > 1:
#     print("enter only single character")
# else:
#     match ch:
#         case 'a'|'e'|'i'|'o'|'u':
#             print('vowel')
#         case _:
#             print("consonent")

'''positive negative zero using guard'''
# num = int(input("enter a number: "))
#
# match num:
#     case num if num > 0:
#         print("positive")
#     case num if num < 0:
#         print("negative")
#     case _:
#         print("zero")


'''menu driven arithmetic program'''
# print("1. addition \t 2. substraction \t 3. multiplication \t 4. division \t 5. exit")
# choice = int(input("enter choice: "))
#
# match choice:
#     case 1:
#         print("performing addition")
#     case 2:
#         print("performing substraction")
#     case 3:
#         print("performing multiplication")
#     case 4:
#         print("performing division")
#     case 5:
#         print("exiting program")
#     case _:
#         print("run program and see the choice again")

'''month days finder'''
# month = int(input("enter month (1 - 12): "))
# match month:
#     case 1|3|5|7|8|10|12:
#         print("31 days")
#     case 4|6|9|11:
#         print("30 days")
#     case 2:
#         print("28/29 days")
#     case _:
#         print("are you from another planet?")

'''grade message system'''
# grade = input("enter your percentage:").upper()
# match grade:
#     case "A":
#         print("excellent")
#     case "B":
#         print("good")
#     case "C":
#         print("avarage")
#     case "D":
#         print("poor")
#     case _:
#         print("failed")

'''Traffic signal system'''
# signal = input("enter signal color: ").lower()
# match signal:
#     case "red":
#         print("gaadi rok de bhai!")
#     case "yellow":
#         print("gaadi start karrrrr!")
#     case "green":
#         print("gaadi leke bhag jaaoo")
#     case _:
#         print("please read traffic signal rules :( ")

'''point position'''
# point = int(input("enter x:")), int(input("enter y: "))
# match point:
#     case (0, 0):
#         print("starting point")
#     case (x, 0):
#         print("on x axis")
#     case (0, y):
#         print("on y axis")
#     case _:
#         print("somewhere else")

'''list size checker'''
# mylist = eval(input("enter list comma separated:"))
#
# match mylist:
#     case [a, b]:
#         print("2 elements are there")
#     case [a, b, c]:
#         print("3 elements are there")
#     case _:
#         print("invalid list size")

'''command handler (start/stop/restart)'''
# command = input("enter command: ")
# match command:
#     case "start":
#         print("system restarting")
#     case "stop":
#         print("system is shutting down")
#     case "restart":
#         print("system restarting")
#     case _:
#         print("invalid command")

'''login system'''
# uname = input("enter username: ").lower()
# pwd = input("enter password: ").lower()
#
# match uname:
#     case uname if uname == "parth":
#         match pwd:
#             case pwd if pwd == "12345":
#                 print("login successful")
#             case _:
#                 print("invalid password")
#     case _:
#         print("invalid username")

'''percentage grading system'''
# percentage = int(input("enter your percentage:"))
# match percentage:
#     case percentage if percentage > 85 and percentage <= 100:
#         print("grade A")
#     case percentage if percentage > 70 and percentage <= 85:
#         print("grade B")
#     case percentage if percentage > 55 and percentage <= 70:
#         print("grade C")
#     case percentage if percentage > 35 and percentage <= 55:
#         print("grade D")
#     case percentage if percentage > 100 or percentage < 0:
#         print("enter valid percentage")
#     case _:
#         print("go to school again")

'''simple chatbot'''
msg = input("say something: ").lower()

match msg:
    case "hi" | "hello" | "hola":
        print("Hey Buddy, how are you?")
    case "bye" | "goodbye":
        print("see you soon!")
    case "help":
        print("sun raha hu !!!")
    case _:
        print("I didn't understand")