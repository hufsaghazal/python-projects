# =============
# Caesar Cipher
# =============


def caesar(
    text, shift, encrypt=True
):  # encrypt=True means we are encrypting by default
    """Encrypt or decrypt text using a Caesar cipher."""

    # Validate the shift and text inputs before processing.
    if not isinstance(shift, int):
        return "Shift must be an integer value."

    if not isinstance(text, str):
        return "Text must be a string."

    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Reverse the shift when decrypting.
    if not encrypt:
        shift = -shift

    # Create the shifted alphabet used for character substitution.
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create a translation table for both lowercase and uppercase letters.
    # Characters not included in the table (spaces, numbers, punctuation)
    # will remain unchanged in the output.
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
    )
    translated_text = text.translate(translation_table)
    return translated_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


def main():
    """Handle user input and run the Caesar cipher."""
    while True:
        choice = input("Encrypt or Decrypt: ").lower().strip()
        text = input("Enter the text to encrypt or decrypt: ")
        try:
            shift = int(input("Enter the shift value (1-25): "))
        except ValueError:
            print("Shift must be an integer value.")
            continue

        if choice == "encrypt":
            print(encrypt(text, shift))

        elif choice == "decrypt":
            print(decrypt(text, shift))
        else:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

        continue_choice = input("Do you want to continue? (yes/no): ").lower().strip()
        if continue_choice == "no":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
