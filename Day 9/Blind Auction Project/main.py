# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)
my_dict = {}

name = input("What is your name? \n")
price = input("Type in the amount that you want to bid $\n")
still_bidding = True
print("\n" * 20)

while still_bidding:
	anyone_else = input("Is anyone else to bid? Please type yes or no \n")
	if anyone_else == "yes":
		new_bidder = input("Please type your name \n")
		new_price = input("Type in the amount that you want to bid \n")
		my_dict[new_bidder] = int(new_price)
		print("\n" * 20)
	elif anyone_else == "no":
		print("Thank you for your participation,please wait fro the bidding results")
		still_bidding = False
	else:
		print("Please type yes or no!")

my_dict[name] = int(price)


highest_bidder = max(zip(my_dict.values(), my_dict.keys()))[1]
print(f"The winner is {highest_bidder} with a total of {my_dict[highest_bidder]} pounds")

