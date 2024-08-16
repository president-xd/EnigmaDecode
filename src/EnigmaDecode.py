import urllib.parse

# Define Base32 characters
BASE32_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

def binary_decode(char: str) -> str:
    """Returns the decrypted text for Binary."""
    if " " not in char and len(char) > 8:
        raise ValueError("Input binary string seems to be missing spaces between bytes.")
    binary_translated = "".join(chr(int(i, 2)) for i in char.strip().split(" "))
    return binary_translated

def hexadecimal_decode(char: str) -> str:
    """Returns the decrypted text for Hexadecimal."""
    if " " not in char and len(char) > 2:
        raise ValueError("Input hexadecimal string seems to be missing spaces between bytes.")
    hexadecimal_translated = "".join(chr(int(i, 16)) for i in char.strip().split(" "))
    return hexadecimal_translated

def octal_decode(char: str) -> str:
    """Returns the decrypted text for Octal."""
    if " " not in char and len(char) > 3:
        raise ValueError("Input octal string seems to be missing spaces between bytes.")
    octal_translated = "".join(chr(int(i, 8)) for i in char.strip().split(" "))
    return octal_translated

def ascii_decode(char: str) -> str:
    """Returns the decrypted text for ASCII."""
    if " " not in char:
        raise ValueError("Input ASCII string seems to be missing spaces between numbers.")
    ascii_translated = "".join(chr(int(i)) for i in str(char).split(" "))
    return ascii_translated

def url_decode(char: str) -> str:
    """Returns the decrypted text for URL Encoding."""
    return urllib.parse.unquote(char)

def unicode_point_decode(char: str) -> str:
    """Returns the decrypted text for Unicode."""
    return "".join(chr(int(uni, 16)) for uni in str(char).split(" "))

def base32_decode(char: str) -> str:
    """Returns the decrypted text for Base32."""
    # Remove padding characters
    char = char.rstrip("=")
    
    # Map Base32 characters to their binary equivalents
    base32_to_bin = {BASE32_ALPHABET[i]: format(i, '05b') for i in range(32)}
    
    # Convert Base32 string to binary string
    binary_string = ''.join(base32_to_bin[c] for c in char)
    
    # Handle padding by calculating the number of padding characters
    padding_length = (8 - len(binary_string) % 8) % 8
    if padding_length > 0:
        binary_string = binary_string[:-padding_length*8]
    
    # Convert binary string to bytes and then to ASCII text
    decoded_bytes = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if byte:
            decoded_bytes.append(int(byte, 2))
    
    # Convert bytes to string
    try:
        decoded_text = decoded_bytes.decode('utf-8')
    except UnicodeDecodeError:
        raise ValueError("Error decoding Base32 string: contains invalid UTF-8 characters")
    
    return decoded_text

def base64_decode(char: str) -> str:
    """Returns the decrypted text for Base64."""
    # Base64 Alphabet
    base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    padding = '='

    # Remove padding characters
    char = char.rstrip(padding)
    
    # Create a dictionary for Base64 to binary conversion
    base64_to_bin = {c: format(i, '06b') for i, c in enumerate(base64_alphabet)}
    
    # Convert Base64 string to binary string
    binary_string = ''.join(base64_to_bin[c] for c in char)
    
    # Handle padding to complete the binary string to byte-aligned length
    if len(binary_string) % 8 != 0:
        binary_string = binary_string[:-((len(binary_string) % 8))]

    # Convert binary string to bytes
    decoded_bytes = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        decoded_bytes.append(int(byte, 2))
    
    # Convert bytes to string
    try:
        decoded_text = decoded_bytes.decode('utf-8')
    except UnicodeDecodeError:
        raise ValueError("Error decoding Base64 string: contains invalid UTF-8 characters")

    return decoded_text

def display_menu():
    print("Choose a decryption method:")
    print("1. Binary")
    print("2. Hexadecimal")
    print("3. Octal")
    print("4. ASCII")
    print("5. URL Encoding")
    print("6. Unicode Point")
    print("7. Base32")
    print("8. Base64")
    print("9. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            char = input("Enter the binary string to decode: ")
            print(f"Decoded text: {binary_decode(char)}")
        elif choice == "2":
            char = input("Enter the hexadecimal string to decode: ")
            print(f"Decoded text: {hexadecimal_decode(char)}")
        elif choice == "3":
            char = input("Enter the octal string to decode: ")
            print(f"Decoded text: {octal_decode(char)}")
        elif choice == "4":
            char = input("Enter the ASCII string to decode: ")
            print(f"Decoded text: {ascii_decode(char)}")
        elif choice == "5":
            char = input("Enter the URL-encoded string to decode: ")
            print(f"Decoded text: {url_decode(char)}")
        elif choice == "6":
            char = input("Enter the Unicode string to decode: ")
            print(f"Decoded text: {unicode_point_decode(char)}")
        elif choice == "7":
            char = input("Enter the Base32 string to decode: ")
            print(f"Decoded text: {base32_decode(char)}")
        elif choice == "8":
            char = input("Enter the Base64 string to decode: ")
            print(f"Decoded text: {base64_decode(char)}")    
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
