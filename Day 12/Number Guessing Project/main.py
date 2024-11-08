import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
list_of_num = range(1, 101)
number_to_be_guessed = random.choice(list_of_num)
print(number_to_be_guessed)
guess_again = True


difficulty = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
if difficulty == "easy":
	attempts = range(10)
	attempts_left = 10
	while guess_again:
		chosen_number_on_easy = int(input("You have 10 attempts to guess the number,please make a guess:"))
		if chosen_number_on_easy != number_to_be_guessed:
			for attempt in attempts:
				while attempts_left != 0:
					attempts_left -= 1
					if attempts_left == 0:
						print(f"""You have failed to guess the number,
	the number you had to guess was {number_to_be_guessed}""")
						attempts_left = 0
						guess_again = False
			if chosen_number_on_easy > number_to_be_guessed:
				print(f"""You have {attempts_left} attempts left,
	the chosen number is high, please guess again""")
			elif chosen_number_on_easy < number_to_be_guessed:
				print(f"""You have {attempts_left} attempts left,
	the chosen number is low, please guess again""")
			elif chosen_number_on_easy == number_to_be_guessed:
				print(f"""Well done the number that 
	you had to guess was indeed {number_to_be_guessed}""")


	# elif difficulty == "hard":
	# 	chosen_number_on_hard = input("You have 5 attempts to guess the number,please make a guess:")
	# else:
	# 	print("Please type easy or hard to play the game")




