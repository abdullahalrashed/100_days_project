print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

##Even odd

number_to_check = int(input("What is the number you want to check?\n"))

if number_to_check % 2 == 0:
    print ("Even")
else:
    print("0dd")

#Nested if/else

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Please pay $5 to ride the rollercoaster")
    elif 18>=age<=12:
        print("Please pay $7 to ride the rollercoaster")
    else:
        print("Please pay $12 to ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")
