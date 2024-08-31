import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# user_moves = [rock, paper, scissors]
cpu_moves = [rock, paper, scissors]

# user_index = random.randint(0, len(user_moves)-1)
cpu_index = random.randint(0, len(cpu_moves)-1)
print(cpu_index)


print("Welcome to Rock, Paper, Scissors game")
user_moves = input("Please type your move\n")
if user_moves == "rock" and cpu_moves[cpu_index] == scissors:
    print(f"USER MOVE : {rock}")
    print(cpu_moves[cpu_index])
    print("User wins")
elif user_moves == "paper" and cpu_moves[cpu_index] == scissors:
    print(f"USER MOVE : {paper}")
    print(cpu_moves[cpu_index])
    print("Cpu wins")
elif user_moves == "scissors" and cpu_moves[cpu_index] == scissors:
    print(f"USER MOVE : {scissors}")
    print(cpu_moves[cpu_index])
    print("Its a draw")

elif user_moves == "rock" and cpu_moves[cpu_index] == paper:
    print(f"USER MOVE : {rock}")
    print(cpu_moves[cpu_index])
    print("Cpu wins")
elif user_moves == "paper" and cpu_moves[cpu_index] == paper:
    print(f"USER MOVE : {paper}")
    print(cpu_moves[cpu_index])
    print("It`s a draw")
elif user_moves == "scissors" and cpu_moves[cpu_index] == paper:
    print(f"USER MOVE : {scissors}")
    print(cpu_moves[cpu_index])
    print("User wins")

elif user_moves == "rock" and cpu_moves[cpu_index] == rock:
    print(f"USER MOVE : {rock}")
    print(cpu_moves[cpu_index])
    print("It`s a draw")
elif user_moves == "paper" and cpu_moves[cpu_index] == rock:
    print(f"USER MOVE : {paper}")
    print(cpu_moves[cpu_index])
    print("User wins")
elif user_moves == "scissors" and cpu_moves[cpu_index] == rock:
    print(f"USER MOVE : {scissors}")
    print(cpu_moves[cpu_index])
    print("Cpu wins")
else:
    print("Please enter valid commands")