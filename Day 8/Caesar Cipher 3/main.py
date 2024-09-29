from art import logo
# TODO-1: Import and print the logo from art.py when the program starts.
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?



def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    decrypted_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shifted_position = alphabet.index(letter) - shift_amount
            decrypted_text += alphabet[shifted_position]

        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]


    if encode_or_decode == "decode":
        print(f"Here is the decoded result: {decrypted_text}")
    elif encode_or_decode == "encode":
        print(f"Here is the {encode_or_decode}d result: {output_text}")

# TODO-3: Can you figure out a way to restart the cipher program?
try_again = True

while try_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))



    if text not in alphabet:
        for letter in text:
            if letter not in alphabet:
                alphabet.append(letter)
                print(alphabet)


    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    try_again = False
    play = input("Type yes if you want to go again, no if you dont!").lower()

    if play == "no":
        try_again = False
        print("Goodbye")
    elif play == "yes":
        try_again = True
