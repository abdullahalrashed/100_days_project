#subscripting
from operator import truediv

print("hello"[-1])

print(2**5)  #power of 2, 2^5
print(5//4)  #remove the decimal point


#large integers
print(123_43_32)
name_user = input("What is your name?\n")
length = len(name_user)
print("Number of letters in you name: " + str(length))

bmi = 84/1.65**2
print(bmi)
bmi = 84/1.65**2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))  ## round it to 2 decimal place number

score =  1
score += 1
print(score)

# turning any type to string by using f
score = 0
height = 1.8
is_winning = True

print(f"your score is = {score},\nyour height is {height},\nYour are winnign is {is_winning}")





