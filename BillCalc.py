bill = float(input("Enter the bill amount: "))
people = int(input("how many people are sharing the bill? "))
salestax = 0.0825
tip_rate = 0.15


tax = bill * salestax

tip = bill * tip_rate

total = bill + tax + tip 

print("restaurant bill")

#calulate amt each person owes
per_person = total / people

#printing everything

print ("Restaurant Bill Calculator")
print("____________________________")
print("Original Bill:  {Bill}")
print("Sales Tax: {tax}" )
print("Tip 15%:  {tip}" )
print("here is the total bill: {total}" )
print("Each person's share: {per_person}")
