import random
uppercase_letters = "ABCDFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*><:;"
all = " "
upper,lower,nums,signs = True,True,True,True
if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if signs:
    all += symbols
length = int(input("Enter the length of the password you want"))
password = "".join(random.sample(all,length))
print("your password is:", password)