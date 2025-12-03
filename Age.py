#Program Description: This program checks the user age confirms their driving eligibiblity
# 
# Variable the store age of user and recieve input 
age = int(input("Enter your age: "))

#if else statment to evalute if user can drive

if(age >= 16):
    print("Your age is eligeible to drive. ")
else:
    print("Your age is ineligeble to drive. ")