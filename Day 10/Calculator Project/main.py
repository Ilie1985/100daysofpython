from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 + n2

def divide(n1, n2):
    return n1 + n2


my_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


first_number = input("Please type in the first number:\n")
mathematical_operator = input("""Please choose the mathematical operator 
for the calculations you want to fulfill:\n(a choice of '+', '-', '*' or '/')\n""")
second_number = input("Please type in the second number:\n")

previous_result = 0
if mathematical_operator == "+":
    my_dict["+"] = int(first_number) + int(second_number)
    previous_result = my_dict["+"]
    print(my_dict["+"])
elif mathematical_operator == "-":
    my_dict["-"] = int(first_number) - int(second_number)
    previous_result = my_dict["-"]
    print(my_dict["-"])
elif mathematical_operator == "*":
    my_dict["*"] = int(first_number) * int(second_number)
    previous_result = my_dict["*"]
    print(my_dict["*"])
elif mathematical_operator == "/":
    my_dict["/"] = int(first_number) / int(second_number)
    previous_result = my_dict["/"]
    print(my_dict["/"])
else:
    print("The app does not recognise your input, please provide valid input")
continue_or_stop = True
while continue_or_stop:

    continue_with_previous_result = input("""Please type "yes" if you want to continue with previous result
"no" if you want to exit the calculation 
"0"-(zero) if you wish to start on a clean slate:\n""").lower()

    if continue_with_previous_result == "yes":
        first_number = input("Please type in the next number:\n")
        mathematical_operator = input("""Please choose the mathematical operator 
for the calculations you want to fulfill-\n (a choice of '+', '-', '*' or '/'):\n""")

        if mathematical_operator == "+":
            my_dict["+"] = previous_result + int(first_number)
            previous_result = my_dict["+"] = previous_result + int(first_number)
            print(my_dict["+"])
        elif mathematical_operator == "-":
            my_dict["-"] = previous_result - int(first_number)
            previous_result = my_dict["-"] = previous_result - int(first_number)
            print(my_dict["-"])
        elif mathematical_operator == "*":
            my_dict["*"] = previous_result * int(first_number)
            previous_result = my_dict["*"] = previous_result * int(first_number)
            print(my_dict["*"])
        elif mathematical_operator == "/":
            my_dict["/"] = previous_result / int(first_number)
            previous_result = my_dict["/"] = previous_result / int(first_number)
            print(my_dict["/"])
        else:
            print("The app does not recognise your input, please provide valid input")
    elif continue_with_previous_result == "no":
        continue_or_stop = False
        print("Thank you for using our app")
    elif int(continue_with_previous_result) == 0:
        first_number = input("Please type in the first number:\n")
        mathematical_operator = input("""Please choose the mathematical operator 
for the calculations you want to fulfill\n(a choice of '+', '-', '*' or '/'):\n""")
        second_number = input("Please type in the second number:\n")
        if mathematical_operator == "+":
            my_dict["+"] = int(first_number) + int(second_number)
            previous_result = my_dict["+"]
            print(my_dict["+"])
        elif mathematical_operator == "-":
            my_dict["-"] = int(first_number) - int(second_number)
            previous_result = my_dict["-"]
            print(my_dict["-"])
        elif mathematical_operator == "*":
            my_dict["*"] = int(first_number) * int(second_number)
            previous_result = my_dict["*"]
            print(my_dict["*"])
        elif mathematical_operator == "/":
            my_dict["/"] = int(first_number) / int(second_number)
            previous_result = my_dict["/"]
            print(my_dict["/"])
        else:
            print("The app does not recognise your input, please provide valid input")

    else:
        continue_or_stop = False
        print("Thank you for using our app")

