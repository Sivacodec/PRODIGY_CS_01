def caesar_cipher(text, shift, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():
            # Determine whether to encrypt or decrypt based on the 'encrypt' parameter
            if encrypt:
                shift_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 
                                 + ord('a' if char.islower() else 'A'))
            else:
                shift_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 
                                 + ord('a' if char.islower() else 'A'))
        else:
            shift_char = char
        result += shift_char
    return result

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (Press 'q' to quit): ").lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (an integer): "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (an integer): "))
            decrypted_message = caesar_cipher(message, shift, encrypt=False)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
