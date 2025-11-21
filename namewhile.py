#variable to store user name
name = input("enter your name: ")

#while loop will run as the variable name has nothing stored in it
while name == "" or not name.isalpha():
    print("invalid name")
    #asking the user to enter their name is case they didn't type 
    name = input("enter your name: ")

 #Exit out of the loop once finished
print(f"hello {name}")

















