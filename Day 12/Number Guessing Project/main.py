import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'").lower()

def num_to_be_guessed():

	list_of_num = range(1, 101)
	n = random.choice(list_of_num)
	return n