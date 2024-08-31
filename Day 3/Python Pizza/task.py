print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
S = 15
M = 20
L = 25
bill = 0

if size == "S":
    if pepperoni == "Y" and extra_cheese == "Y":
        bill = S + 2 + 1
        print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "Y" and pepperoni == "N":
        bill = S + 1
        print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "N" and pepperoni == "Y":
        bill = S + 2
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${S}.")
elif size == "M":
    if pepperoni == "Y" and extra_cheese == "Y":
        bill = M + 3 + 1
        print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "Y" and pepperoni == "N":
        bill = M + 1
        print(f"Your final bill is\n ${bill}.")
    elif extra_cheese == "N" and pepperoni == "Y":
        bill = M + 3
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${M}.")
elif size == "L":
    if pepperoni == "Y" and extra_cheese == "Y":
        bill = L + 3 + 1
        print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "Y" and pepperoni == "N":
        bill = L + 1
        print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "N" and pepperoni == "Y":
        bill = L + 3
        print(f"Your final bill is: ${bill}.")
    elif pepperoni == "N" and extra_cheese == "N":
        print(f"Your final bill is: ${L}.")
else:
    print("please enter the correct details")
