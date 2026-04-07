fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score
print(sum)

score2 = student_scores[0]

for Max_value in student_scores:
    if Max_value > score2:
        score2 = Max_value
print(score2)
