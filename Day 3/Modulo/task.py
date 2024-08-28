print("Welcome to modulo lesson")
chosen_number = input("Please input a number")
input_transformed_to_number = int(chosen_number)
print(type(input_transformed_to_number))
print(input_transformed_to_number % 2)
if input_transformed_to_number % 2 == 0:
    print("Your chosen number is an even number")
else:
    print("Your chosen number is odd")
