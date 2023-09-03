import random
import string
import argparse

def generate_password(length, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("--uppercase", action="store_true", help="Include uppercase letters (default: False)")
    parser.add_argument("--digits", action="store_true", help="Include digits (default: False)")
    parser.add_argument("--special-chars", action="store_true", help="Include special characters (default: False)")

    args = parser.parse_args()

    password = generate_password(args.length, args.uppercase, args.digits, args.special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
