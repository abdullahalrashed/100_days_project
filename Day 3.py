# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n"))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")
#
# ##Even odd
#
# number_to_check = int(input("What is the number you want to check?\n"))
#
# if number_to_check % 2 == 0:
#     print ("Even")
# else:
#     print("0dd")
#
# #Nested if/else
#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n"))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?\n"))
#     if age < 12:
#         print("Please pay $5 to ride the rollercoaster")
#     elif 18>=age<=12:
#         print("Please pay $7 to ride the rollercoaster")
#     else:
#         print("Please pay $12 to ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")
#
# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# # 🚨 Do not modify the values above
# # Write your code below 👇
#
# if bmi <18.5:
#     print("underweight")
# elif 18.5 <= bmi < 25:
#     print("Normal")
# else:
#     print("Overweight")
#
# #multiple if statement in succesion
#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n"))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.\n")
#     if wants_photo == "y":
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# Excercise

print("Welcome to Python Pizza Deliveries!")
size = input("What is your size? S for small, Medium for M, L for large?\n")
price = 0
if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        price += 2
    elif size in "M , L": ## if size == "M" or size == "L":
        price += 3
else :
    price += 0
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    price += 1
else:
    price += 0
print(f"your Final price is ${price}")

