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
