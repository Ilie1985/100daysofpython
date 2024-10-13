from art import logo
import random


begin_game = input("Do you want to play a game of BlackJAck? Type 'y' or 'n' :").lower()

if begin_game == "y":
	print(logo)

	jack_dame_pope = {
		"jack": 10,
		"dame": 10,
		"pope": 10
	}
	cards = [11,2,3,4,5,6,7,8,9,10, jack_dame_pope["jack"], jack_dame_pope["dame"], jack_dame_pope["pope"]]

	first_card = random.choice(cards)
	second_card = random.choice(cards)

	cpu_first_card = random.choice(cards)
	cpu_second_card = random.choice(cards)
	cpus_first_cards = cpu_first_card + cpu_second_card

	users_first_cards = first_card + second_card
	print(f"your first cards [ {first_card}, {second_card} ]: {users_first_cards}")
	print(f"cpu`s first cards [ {cpu_first_card}, {cpu_second_card} ]: {cpus_first_cards}")
	if users_first_cards > 21 and cpus_first_cards <= 21:
		print(f"Your score is {users_first_cards}")
		print(f"Cpus score is {cpus_first_cards}")
		print("You lose")
	elif cpus_first_cards > 21 and users_first_cards <= 21:
		print(f"Your score is {users_first_cards}")
		print(f"Cpus score is {cpus_first_cards}")
		print("You win")

	user_asks_for_another_card = input("Do you want another card? Please type 'y' or 'n': ").lower()
	ask_for_cards = True

	while ask_for_cards:
		if user_asks_for_another_card == "y":

			users_new_card = random.choice(cards)
			print(f"This is your new card {users_new_card}")
			users_first_cards += users_new_card
			print(f"Your new total is : ' {users_first_cards} '")

			if users_first_cards > 21:

				print(f"You loser")
				ask_for_cards = False
				break
			cpu_new_card = random.choice(cards)
			print(f"This is cpu`s new card: {cpu_new_card}")
			cpus_first_cards += cpu_new_card
			print(f"Cpu`s new total is : ' {cpus_first_cards} '")

			if users_first_cards > 21:
				# print(f" Your score is: {users_first_cards}")
				print("You lose, sorry")
				ask_for_cards = False
				break
			elif cpus_first_cards > 21:
				print("You win, good job")
				ask_for_cards = False
				break
			elif users_first_cards <= 21:
				user_asks_for_another_card = input("Do you want another card? Please type 'y' or 'n':").lower()
			else:
				if users_first_cards > cpus_first_cards and users_first_cards <= 21:
					print(f"Your score is: {users_first_cards}")
					print(f"Cpu score is: {cpus_first_cards}")
					print("Congratulations ,you win")
					ask_for_cards = False
				elif users_first_cards > cpus_first_cards and users_first_cards > 21:
					print(f"Your score is: {users_first_cards}")
					print(f"Cpu score is: {cpus_first_cards}")
					print("You lose!")
					ask_for_cards = False
				elif users_first_cards < cpus_first_cards and cpus_first_cards <= 21:
					print(f"Your score is: {users_first_cards}")
					print(f"Cpu score is: {cpus_first_cards}")
					print("You lose!")
					ask_for_cards = False
				elif users_first_cards == cpus_first_cards:
					print(f"Your score is: {users_first_cards}")
					print(f"Cpu score is: {cpus_first_cards}")
					print("It`s a draw!")
					ask_for_cards = False
				elif cpus_first_cards > 21 and users_first_cards <= 21:
					print(f"Your score is: {users_first_cards}")
					print(f"Cpu score is: {cpus_first_cards}")
					print("Congratulations ,you win")

		elif user_asks_for_another_card == "n":
			if users_first_cards > cpus_first_cards and users_first_cards <= 21:
				print(f"Your score is: {users_first_cards}")
				print(f"Cpu score is: {cpus_first_cards}")
				print("Congratulations ,you win")
				ask_for_cards = False
			elif users_first_cards > cpus_first_cards and users_first_cards > 21:
				print(f"Your score is: {users_first_cards}")
				print(f"Cpu score is: {cpus_first_cards}")
				print("You lose!")
				ask_for_cards = False
			elif users_first_cards < cpus_first_cards and cpus_first_cards <= 21:
				print(f"Your score is: {users_first_cards}")
				print(f"Cpu score is: {cpus_first_cards}")
				print("You lose!")
				ask_for_cards = False
			elif users_first_cards == cpus_first_cards :
				print(f"Your score is: {users_first_cards}")
				print(f"Cpu score is: {cpus_first_cards}")
				print("It`s a draw!")
				ask_for_cards = False
			elif users_first_cards == 21 and cpus_first_cards < 21:
				print(f"Your score is: {users_first_cards}")
				print(f"Cpu score is: {cpus_first_cards}")
				print("Congratulations ,you win")


elif begin_game == "n":
	print("See you soon!")









