def encrypt(text, shift):
    result = ""
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice! Please enter 'e' or 'd'.")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted message: {encrypted_text}")
    else:
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
