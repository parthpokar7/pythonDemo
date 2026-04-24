import re

# email = input("enter email address:")
# email = "parth@gmail.com"
email = "parth_pokar@gmail.in"
# email = "parth.pokar@gmail.com"
# email = "0parth@gmail.com"
# email = "parthpoart@gmail.coms"

pattern = r"^[a-zA-Z]+[\w.]+@+[\w.]+[.]+(com|in)$"
print(re.match(pattern, email))
if re.match(pattern, email):
    print("valid email")
else:
    print("invalid email")



pwd = "aAb!1"


pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$&])"
print(re.match(pattern, pwd))
if re.match(pattern, pwd):
    print("valid pass")
else:
    print("invalid pass")


num = "9955443322"
pattern = r"^[9]\d{9}$"
print(re.match(pattern, num))
if re.match(pattern, num):
    print("valid number")
else:
    print("invalid number")

pin = "220002"
pattern = r"^\d{6}$"
print(re.match(pattern, pin))
if re.match(pattern, pin):
    print("valid pin")
else:
    print("invalid pin")

username = "part343"
pattern = r"^[a-zA-Z]\w{4,}$"

print(re.match(pattern, username))
if re.match(pattern, username):
    print("valid username")
else:
    print("invalid username")