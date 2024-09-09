import string

def caesar_cipher(text, shift, encrypt=True):
    result = []
    shift = shift if encrypt else -shift
    for char in text:
        if char in string.ascii_lowercase:
            # Shift lowercase letters
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif char in string.ascii_uppercase:
            # Shift uppercase letters
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            # Non-alphabetical characters are unchanged
            result.append(char)
    return ''.join(result)

def encrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as f:
            content = f.read()

        encrypted_content = caesar_cipher(content, shift)

        with open(output_file, 'w') as f:
            f.write(encrypted_content)

        print(f"File '{input_file}' encrypted successfully and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as f:
            content = f.read()

        decrypted_content = caesar_cipher(content, shift, encrypt=False)

        with open(output_file, 'w') as f:
            f.write(decrypted_content)

        print(f"File '{input_file}' decrypted successfully and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    action = input("Would you like to (E)ncrypt or (D)ecrypt a file? ").lower()
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    shift = int(input("Enter the shift value (1-25): "))

    if action == 'e':
        encrypt_file(input_file, output_file, shift)
    elif action == 'd':
        decrypt_file(input_file, output_file, shift)
    else:
        print("Invalid choice. Please select 'E' for encrypt or 'D' for decrypt.")

if __name__ == "__main__":
    main()
