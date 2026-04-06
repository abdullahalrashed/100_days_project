import random

random_integer = random.randint(1, 10)
print(random_integer)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

states_of_america[1] = "Pengilvania"

states_of_america.append("Angelaland")
states_of_america.extend(["Angelaland2", "Jack Bauer Land"])
print(states_of_america)

number = random.randint(0, 4)
friends = ["alice", "Bob", "Charlie", "David", "Emanuel"]
name = friends[number]
print(name)

friends2 = ["alice", "Bob", "Charlie", "David", "Emanuel"]
name2 = random.choice(friends2)
print(name2)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0][0])

# rock paper scissors game

rock = (''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''')

scissors = ('''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

art = [rock, paper, scissors]
names = ["rock", "paper", "scissors"]
computer_choice = random.choice(names)
user_choice = input("Choose between Rock, Paper, or Scissors:\n").lower()

if computer_choice == user_choice:
    print(f"Computer chose {computer_choice} and you chose {user_choice}")
    print("It's a tie!")
elif computer_choice == "rock" and user_choice == "paper":
    print(f"Computer chose {computer_choice}:")
    print(rock)
    print(f"and you chose {user_choice}")
    print(paper)
    print("You win!")
elif computer_choice == "rock" and user_choice == "scissors":
    print(f"Computer chose {computer_choice}:")
    print(rock)
    print(f"and you chose {user_choice}")
    print(scissors)
    print(" computer Wins")
elif computer_choice == "paper" and user_choice == "rock":
    print(f"Computer chose {computer_choice}:")
    print(paper)
    print(f"and you chose {user_choice}")
    print(paper)
    print("Computer Wins!")
elif computer_choice == "paper" and user_choice == "scissors":
    print(f"Computer chose {computer_choice}:")
    print(paper)
    print(f"and you chose {user_choice}")
    print(scissors)
    print("You win!")
elif computer_choice == "scissors" and user_choice == "paper":
    print(f"Computer chose {computer_choice}:")
    print(scissors)
    print(f"and you chose {user_choice}")
    print(paper)
    print("Computer Wins!")
elif computer_choice == "scissors" and user_choice == "rock":
    print(f"Computer chose {computer_choice}:")
    print(scissors)
    print(f"and you chose {user_choice}")
    print(rock)
    print("You win!")
else:
    print("You chose a wrong choice. Try again.")

# another way to code
rock = (''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''')

scissors = ('''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
# 0, 1, 2
if 0 <= user_choice <= 2:
    print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")

elif user_choice == 0 and computer_choice == 2:
    print("You win!")

elif computer_choice == 0 and user_choice == 2:
    print("You lose!")

elif computer_choice > user_choice:
    print("You lose!")

elif user_choice > computer_choice:
    print("You win!")

elif computer_choice == user_choice:
    print("It's a draw!")
