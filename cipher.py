# Kristen Crowe Caesar-cipher assignment 
# Used notes from class and online resources to complete

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the base value for lowercase and uppercase
            base = ord('a') if char.islower() else ord('A')
            # Shift the character within the alphabet and wrap around using modulo
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_text += char
    return encrypted_text

# Asking the user for input
sentence = input("Please enter a sentence: ")

# Change the characters using a shift to the right 5 positions
shift = 5
encrypted_sentence = caesar_cipher(sentence, shift)

# Print the new sentence
print(f"The encrypted sentence is: {encrypted_sentence}")
