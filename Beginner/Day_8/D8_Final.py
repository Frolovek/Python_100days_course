import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode, original_text, shift_amount):
    message = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for i in original_text:

        # My solution instead of using %
        # if new_index > len(alphabet):
        #     new_index -= len(alphabet)
        #     encrypted_message += alphabet[new_index]
        # else:
        #     encrypted_message += alphabet[new_index]

        # My solution instead of using *= -1
        # if encode_or_decode == "encode":
        #     new_index = alphabet.index(i) + shift_amount
        # elif encode_or_decode == "decode":
        #     new_index = alphabet.index(i) - shift_amount
        if i in alphabet:
            new_index = alphabet.index(i) + shift_amount
            new_index %= len(alphabet)
            message += alphabet[new_index]
        else:
            message += i
    print(f"Here is the {encode_or_decode}d result: {message}")

is_continue = "yes"

while is_continue == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    is_continue = input("Would you like o continue? Type 'yes' or 'no': \n").lower()

print("Goodbye")
