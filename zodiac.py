import argparse

def custom_rot_cipher(input_str, shift, mode):
    # English alphabet + Zodiac symbols
    custom_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ♈♉♊♋♌♍♎♏♐♑♒♓'
    result = ''

    # Adjust shift for decoding
    if mode == 'decode':
        shift = -shift

    for char in input_str:
        if char.upper() in custom_alphabet:
            # Find the index in the custom alphabet (considering case)
            is_uppercase = char.isupper()
            index = custom_alphabet.find(char.upper())

            # Shift the index by the specified shift value
            shifted_index = (index + shift) % len(custom_alphabet)

            # Add the shifted character to the result
            if is_uppercase:
                result += custom_alphabet[shifted_index]
            else:
                result += custom_alphabet[shifted_index].lower()
        else:
            # Leave characters not in the custom alphabet unchanged
            result += char

    return result

def main():
    parser = argparse.ArgumentParser(description='Custom ROT cipher with Zodiac symbols.')
    parser.add_argument('mode', type=str, choices=['encode', 'decode'], help='Mode of operation: encode or decode.')
    parser.add_argument('shift', type=int, help='Shift value for the cipher.')
    parser.add_argument('message', type=str, help='Message to encode or decode.')
    
    args = parser.parse_args()

    transformed_message = custom_rot_cipher(args.message, args.shift, args.mode)
    print(transformed_message)

if __name__ == "__main__":
    main()

