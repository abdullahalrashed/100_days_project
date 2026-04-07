# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)
#
# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
# # finding how th efunction SUM works
#
# total_exam_score = sum(student_scores)
#
# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)
#
# # Finding how the function MAX works
# # type 1
# score2 = student_scores[0]
#
# for Max_value in student_scores:
#     if Max_value > score2:
#         score2 = Max_value
# print(score2)
#
# # type 2
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)
#
# #range function
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)
#
#     # for steps by 3
# for number in range(1, 101, 3):
#     print(number)

# A fizzbuzz game

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# PASSWORD GENERATOR
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', "'", '*', '+']

print("Welcome to the PyPassword Generator!")
password = ""
nr_letters = int(input("How many letters would you Like in your password?\n"))
if nr_letters <= 0 or nr_letters > 26:
    print("Please enter a number between 1 and 26.")
for char in range(0, nr_letters):
    password += random.choice(letters)
np_symbols = int(input(f"How many symbols would you like?\n"))
if np_symbols <= 0 or np_symbols > 8:
    print("Please enter a number between 1 and 8")
for symbol in range(0, np_symbols):
    password += random.choice(symbols)
nr_numbers = int(input(f"How many numbers would you like?\n"))
if nr_numbers < 0 or nr_numbers > 10:
    print("Please enter a number between 0 and 10")
for number in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)

# hard mode
