#Creating the function
def get_user_name():
    name = input("What is your name?")
    print("Hello, " + name)


#Outside the function
print("Hello")
get_user_name() # Calling the function