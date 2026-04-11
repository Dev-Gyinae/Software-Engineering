# Caesar's Cipher
alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

def get_valid_direction():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ["encode", "decode"]:
            return direction
        print("Invalid input! Please type 'encode' or 'decode'.")

def get_valid_shift():
    while True:
        try:
            shift = int(input("Type the shift number (1-25):\n"))
            if 1 <= shift <= 25:
                return shift
            print("Please enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

should_continue = True

while should_continue:
    direction = get_valid_direction()
    text = input("Type your message:\n").lower()
    shift = get_valid_shift()
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    while True:
        result = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
        if result in ["yes", "no"]:
            if result == "no":
                should_continue = False
                print("Goodbye!")
            break
        print("Invalid input! Please type 'yes' or 'no'.")