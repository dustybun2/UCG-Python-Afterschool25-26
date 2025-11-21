#program name: Login simulator program 
#program description This program simulates a login system.
# The user must enter the correct password within three tries or they're locked out.

# The correct password
password = "python123" 

# variable to store user input
attempt =""

# Track the number of tries
tries = 0

# Loop continues while the password is wrong AND user has tries left
while attempt != password and tries < 3:
 attempt = imput ("Enter the password ") #Ask user to type the password
tries += 1 # Add 1 to the number of tries

# check if the password is wrong
if attempt != password:
 print("incorrect password! try again")

#once loop ends, checks why it ended
if attempt == password:
    print("✅ access granted!") #if password is correct
else:
    print("🚫Too many attempt, Try later.") #if user ran out of tries
