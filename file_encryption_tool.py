import string

# Function to perform Caesar Cipher encryption/decryption
def caesar_cipher(text, shift, encrypt=True):
    # Initialize an empty list to store the result
    result = []
    
    # If decrypting, we negate the shift value (to reverse the process)
    shift = shift if encrypt else -shift
    
    # Loop through each character in the input text
    for char in text:
        # Check if the character is a lowercase letter
        if char in string.ascii_lowercase:
            # Shift the character and wrap it using modulo 26 (for 26 letters in the alphabet)
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        # Check if the character is an uppercase letter
        elif char in string.ascii_uppercase:
            # Shift the character and wrap it using modulo 26 (for 26 letters in the alphabet)
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            # If it's not a letter, leave the character unchanged
            result.append(char)
    
    # Return the joined list as a string (the final encrypted/decrypted text)
    return ''.join(result)

# Function to encrypt the content of a file
def encrypt_file(input_file, output_file, shift):
    try:
        # Print which file is being opened (for debugging purposes)
        print(f"Opening file: {input_file}")
        
        # Open the input file in read mode ('r')
        with open(input_file, 'r') as f:
            # Read the file's content
            content = f.read()

        # Encrypt the content using the Caesar Cipher
        encrypted_content = caesar_cipher(content, shift)

        # Open (or create) the output file in write mode ('w') and save the encrypted content
        with open(output_file, 'w') as f:
            f.write(encrypted_content)

        # Print a success message
        print(f"File '{input_file}' encrypted successfully and saved as '{output_file}'.")
    except FileNotFoundError:
        # If the input file doesn't exist, print an error message
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        # Catch any other exceptions and print the error message
        print(f"An error occurred: {e}")

# Function to decrypt the content of a file
def decrypt_file(input_file, output_file, shift):
    try:
        # Print which file is being opened (for debugging purposes)
        print(f"Opening file: {input_file}")
        
        # Open the input file in read mode ('r')
        with open(input_file, 'r') as f:
            # Read the file's content
            content = f.read()

        # Decrypt the content using the Caesar Cipher (with encryption set to False)
        decrypted_content = caesar_cipher(content, shift, encrypt=False)

        # Open (or create) the output file in write mode ('w') and save the decrypted content
        with open(output_file, 'w') as f:
            f.write(decrypted_content)

        # Print a success message
        print(f"File '{input_file}' decrypted successfully and saved as '{output_file}'.")
    except FileNotFoundError:
        # If the input file doesn't exist, print an error message
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        # Catch any other exceptions and print the error message
        print(f"An error occurred: {e}")

# Main function to handle user input and trigger encryption or decryption
def main():
    # Ask the user if they want to encrypt or decrypt a file
    action = input("Would you like to (E)ncrypt or (D)ecrypt a file? ").lower()
    
    # Get the input file name from the user
    input_file = input("Enter the name of the input file: ")
    
    # Get the output file name (where the encrypted or decrypted content will be saved)
    output_file = input("Enter the name of the output file: ")
    
    # Ask the user for the shift value (which determines how much to shift the characters)
    shift = int(input("Enter the shift value (1-25): "))

    # If the user chooses to encrypt, call the encrypt_file function
    if action == 'e':
        encrypt_file(input_file, output_file, shift)
    # If the user chooses to decrypt, call the decrypt_file function
    elif action == 'd':
        decrypt_file(input_file, output_file, shift)
    # If the input is invalid, display an error message
    else:
        print("Invalid choice. Please select 'E' for encrypt or 'D' for decrypt.")

# Entry point of the script
if __name__ == "__main__":
    main()
