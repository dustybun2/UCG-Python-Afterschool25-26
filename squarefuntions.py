# program description:
# this program defines a function that takes a number
# and return it's square.

#define the function
def square(num):
    return num * num 

# Ask the user for a number
n = int(input("Enter the number:"))

# Call the function and show the result
print(f"The square of {n} is {square(n)}")