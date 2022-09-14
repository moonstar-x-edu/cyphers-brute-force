import sys
import re


ASCII_OFFSET = 97
ALPHABET_SIZE = 26


def clean_message(message: str) -> str:
    return re.sub(r'[^a-z ]', '', message.lower())


def encode(message: str, key: int) -> str:
    return ''


def decode(message: str, key: int) -> str:
    return ''


def brute_force(message: str) -> list:
    return []


def main():
    original_message = sys.argv[1]
    print(f'Original message: {original_message}')

    cleaned_message = clean_message(original_message)
    print(f'Clean message: {cleaned_message}')

    encoded = encode(cleaned_message, 5)
    print(f'Encoded message: {encoded}')

    guesses = brute_force(encoded)
    for d in guesses:
        print(f'Potentially decoded message: {d}')

    print(f'Found?: {any(map(lambda d: d == cleaned_message, guesses))}')


if __name__ == '__main__':
    main()
