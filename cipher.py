def encrypt(text, shift):
    result = ""
    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetic characters are not changed
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please try again.")
            continue

        text = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        elif choice == 'd':
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
