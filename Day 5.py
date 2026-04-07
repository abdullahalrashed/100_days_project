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

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# PASSWORD GENERATOR
