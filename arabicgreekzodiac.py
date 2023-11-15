import argparse

def custom_rot_cipher(input_str, shift, mode, null_symbol=None):
    # Combined English, Zodiac, Greek, and Arabic alphabets
    custom_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ♈♉♊♋♌♍♎♏♐♑♒♓ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩابتثجحخدذرزسشصضطظعغفقكلمنهوي'
    result = ''

    # Adjust shift for decoding
    if mode == 'decode':
        shift = -shift

    for char in input_str:
        if char == null_symbol:
            # Ignore the null symbol
            continue

        # Check if character is upper case or in a non-Latin alphabet
        is_uppercase = char.isupper() and char.isascii()
        char_to_find = char.upper() if is_uppercase else char

        if char_to_find in custom_alphabet:
            # Find the index in the custom alphabet
            index = custom_alphabet.find(char_to_find)

            # Shift the index by the specified shift value
            shifted_index = (index + shift) % len(custom_alphabet)
            shifted_char = custom_alphabet[shifted_index]

            # Convert back to lowercase if original char was lowercase
            if not is_uppercase and char.isascii():
                shifted_char = shifted_char.lower()
            result += shifted_char
        else:
            # Leave characters not in the custom alphabet unchanged
            result += char

    return result

def main():
    parser = argparse.ArgumentParser(description='Custom ROT cipher with Zodiac, Greek, and Arabic symbols.')
    parser.add_argument('mode', type=str, choices=['encode', 'decode'], help='Mode of operation: encode or decode.')
    parser.add_argument('shift', type=int, help='Shift value for the cipher.')
    parser.add_argument('message', type=str, help='Message to encode or decode.')
    parser.add_argument('--null_symbol', type=str, default=None, help='Optional null symbol to be ignored in the cipher.')

    args = parser.parse_args()

    transformed_message = custom_rot_cipher(args.message, args.shift, args.mode, args.null_symbol)
    print(transformed_message)

if __name__ == "__main__":
    main()

