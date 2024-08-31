# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

# name = input("What is your name?: ")
# age = input("How old are you?: ")
# age = int(age) + 1
#
# print(f"Hello, {name}! Nice to meet you!")
# print("HAPPY BIRTHDAY!")
# print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc

# length = input("Enter the length: ")
# width = input("Enter the width: ")
# unit = input("Enter the unit: ")
# area = float(length) * float(width)
# print(f"The rectangle area is {area} {unit}²")

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"The total is: PLN{round(total, 2)}")

