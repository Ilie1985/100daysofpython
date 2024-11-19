import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print("You get 10 guesses for 'easy' level and 5 guesses for 'hard' level.")
list_of_num = range(1, 101)
number_to_be_guessed = random.choice(list_of_num)

guess_again = True
attempts_left_on_easy = 10
attempts_left_on_hard = 5
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

while guess_again:
	chosen_number = int(input(f"Try to guess the number,please make a guess:\n"))
	if difficulty == "easy" and number_to_be_guessed != chosen_number:
		attempts_left_on_easy -= 1

		if attempts_left_on_easy < 10 and attempts_left_on_easy != 0:
			print(f"you have {attempts_left_on_easy} guesses left ,try again:\n")
		elif attempts_left_on_easy == 0:
			print(
				f"you have {attempts_left_on_easy} guesses left, you lost the game!The number to be guessed was {number_to_be_guessed}")
			guess_again = False
	elif difficulty == "easy" and number_to_be_guessed == chosen_number:
		print(f"Congrats, the number to be guessed was: {number_to_be_guessed}")
		guess_again = False

	if difficulty == "hard" and number_to_be_guessed != chosen_number:
		attempts_left_on_hard -= 1

		if attempts_left_on_hard < 5 and attempts_left_on_hard != 0:
			print(f"you have {attempts_left_on_hard} guesses left ,try again")
		elif attempts_left_on_hard == 0:
			print(
				f"you have {attempts_left_on_hard} guesses left, you lost the game!The number to be guessed was {number_to_be_guessed}")
			guess_again = False
	elif difficulty == "hard" and number_to_be_guessed == chosen_number:
		print(f"Congrats, the number to be guessed was {number_to_be_guessed}")
		guess_again = False




