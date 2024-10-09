from art import logo
import random

start_or_end_game = input("Do you want to play a game of BlackJAck? Type 'y' or 'n'").lower()
if start_or_end_game == "y":
	print(logo)
elif start_or_end_game == "n":
	print("See you soon!")


jack_dame_pope = {
	"jack": 10,
	"dame": 10,
	"pope": 10
}
cards = [11,2,3,4,5,6,7,8,9,10, jack_dame_pope["jack"], jack_dame_pope["dame"], jack_dame_pope["pope"]]

first_card = random.choice(cards)
second_card = random.choice(cards)

first_cards = first_card + second_card
print(first_card)
print(second_card)
print(first_cards)

