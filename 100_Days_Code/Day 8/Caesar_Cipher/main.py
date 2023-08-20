# Create list of alphabet or find builtin that includes a list of alphabet
# I TRIED TO LOOP AROUND THE LIST BUT IT WOULD BE SIMPLER TO JUST ADD THE CONTENTS OF THE LIST TWICE SO NO LOOPING IS NEEDED WHICH WOULD ALLOW ME TO COMBINE THE DECRPYT AND ENCRYPT FUNCTIONS INTO ONE FUNCTION
# I WAS THINKING IN C AGAIN.  PYTHON USES NEGATIVE NUMBERS TO LOOP AROUND LISTS.
# MY VERSION IS NOT PYTHONIC

from hashlib import new

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# print(alphabet[-5])

# # Get either 'encode' to encrypt or 'decode' to decrypt from user input
encode_or_decode = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt. ").lower()

# # Get the message to encrypt or decode from user input and use .lower() for easier comparison
if encode_or_decode == "encode":
    message = input("Please enter your message to encode: ").lower()
else:
    message = input("Please enter your message to decode: ").lower()

# # Get the shift value from user input and cast as int()
shift = int(input("Please enter the shift value as an integer: "))


# Function to encrypt using the message and shift variables
def encrypt(message_to_encrypt, shift_value):
    encrypted_message = ""
    for letter in message_to_encrypt:
        new_index = alphabet.index(letter) + shift_value
        message_length = len(alphabet)

        # Test if the current index is greater than the length of the encrypted message
        if new_index > message_length - 1:
            new_index = new_index - message_length

        encrypted_message += alphabet[new_index]
    return encrypted_message


# Function to decrypt using the message and shift variables
def decrypt(message_to_decrypt, shift_value):
    decrypted_message = ""
    for letter in message_to_decrypt:
        new_index = alphabet.index(letter) - shift_value

        # Test if the current index needs to wrap to end of alphabet
        if new_index < 0:
            new_index = len(alphabet) + new_index

        decrypted_message += alphabet[new_index]
    return decrypted_message


if encode_or_decode == "encode":
    encoded_message = encrypt(message_to_encrypt=message, shift_value=shift)
    print(f"The encoded text is {encoded_message}")
else:
    decoded_message = decrypt(message_to_decrypt=message, shift_value=shift)
    print(f"The decoded text is {decoded_message}")
