"""
--------------------------------------------------------
    Caesar Cipher Project - Full Working Code
    Features:
        ✓ Encryption
        ✓ Decryption
        ✓ Brute-Force Cracking
        ✓ Frequency Analysis
--------------------------------------------------------
"""


import string
from collections import Counter


# -------------------------------------
# Caesar Cipher: Encrypt Function
# -------------------------------------
def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():  
            alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
            new_pos = (alphabet.index(char) + key) % 26
            result += alphabet[new_pos]
        else:
            result += char  # Keep spaces & punctuation
    return result


# -------------------------------------
# Caesar Cipher: Decrypt Function
# -------------------------------------
def decrypt(text, key):
    return encrypt(text, -key)


# -------------------------------------
# Brute Force Attack
# -------------------------------------
def brute_force(ciphertext):
    print("\n===== Brute Force Results =====")
    for key in range(26):
        print(f"Key {key}: {decrypt(ciphertext, key)}")


# -------------------------------------
# Frequency Analysis (Guess the Key)
# -------------------------------------

def frequency_analysis(ciphertext):
    # Only keep letters
    letters = [c.upper() for c in ciphertext if c.isalpha()]
    if not letters:
        print("No letters to analyze!")
        return

    # Count frequency of each character
    freq = Counter(letters)

    # Most common letter in the ciphertext
    most_common, _ = freq.most_common(1)[0]

    # Assume that most common letter maps to 'E'
    assumed_key = (ord(most_common) - ord('E')) % 26

    print("\n===== Frequency Analysis =====")
    print(f"Most common letter: {most_common}")
    print(f"Estimated key: {assumed_key}")
    print("Estimated Plaintext:")
    print(decrypt(ciphertext, assumed_key))


# -------------------------------------
# Main Menu System
# -------------------------------------
def menu():
    while True:
        print("\n===================================")
        print("         CAESAR CIPHER TOOL        ")
        print("===================================")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Brute Force Crack")
        print("4. Frequency Analysis")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            text = input("Enter plaintext: ")
            key = int(input("Enter key (0-25): "))
            print("\nEncrypted text:", encrypt(text, key))

        elif choice == "2":
            text = input("Enter ciphertext: ")
            key = int(input("Enter key (0-25): "))
            print("\nDecrypted text:", decrypt(text, key))

        elif choice == "3":
            text = input("Enter ciphertext: ")
            brute_force(text)

        elif choice == "4":
            text = input("Enter ciphertext: ")
            frequency_analysis(text)

        elif choice == "5":
            print("Exiting program… Goodbye!")
            break

        else:
            print("Invalid choice! Please choose between 1–5.")


# -------------------------------------
# Program Entry Point
# -------------------------------------
if __name__ == "__main__":
    menu()
