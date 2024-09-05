import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
display = ""
guess = input("Guess a letter: ").lower()


for letter in chosen_word:
    placeholder = placeholder + "_"
    print(placeholder)
if guess in chosen_word:
    display += guess
    print(display)
elif guess not in chosen_word:
    display += "_"


# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.


# for letter in chosen_word:
#     if guess in chosen_word:
#         display += letter
#         print(display)
#
#     elif letter not in chosen_word:
#         display += "_"






