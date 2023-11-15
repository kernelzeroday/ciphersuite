import argparse

def create_mapping_for_encoding(english_alphabet, selected_alphabets, shift):
    mapping = {}
    for i, char in enumerate(english_alphabet):
        mapped_char = selected_alphabets[(i + shift) % len(selected_alphabets)]
        mapping[char] = mapped_char
    return mapping

def create_mapping_for_decoding(english_alphabet, selected_alphabets, shift):
    mapping = {}
    shifted_alphabets = selected_alphabets[shift:] + selected_alphabets[:shift]
    for i, char in enumerate(shifted_alphabets):
        mapped_char = english_alphabet[i % len(english_alphabet)]
        mapping[char] = mapped_char
    return mapping

def custom_rot_cipher(input_str, shift, mode, alphabets, alphabets_dict, null_symbol=None):
    english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    selected_alphabets = ''.join(alphabets_dict[char] for char in alphabets if char in alphabets_dict)

    if mode == 'encode':
        mapping = create_mapping_for_encoding(english_alphabet, selected_alphabets, shift)
    elif mode == 'decode':
        mapping = create_mapping_for_decoding(english_alphabet, selected_alphabets, shift)

    result = ''

    for char in input_str:
        if char == null_symbol:
            continue

        result += mapping.get(char, char)

    return result

def main():
    parser = argparse.ArgumentParser(description='Custom ROT cipher with multiple selectable alphabets for encoding and decoding English text.')
    parser.add_argument('mode', type=str, choices=['encode', 'decode'], help='Mode of operation: encode or decode.')
    parser.add_argument('shift', type=int, help='Shift value for the cipher.')
    parser.add_argument('message', type=str, help='Message to encode or decode.')
    parser.add_argument('--alphabets', type=str, default='E', help='Alphabets to use: E for English, Z for Zodiac, G for Greek, A for Arabic, P for Planetary, J for Japanese, S for Scientific.')
    parser.add_argument('--null_symbol', type=str, default=None, help='Optional null symbol to be ignored in the cipher.')

    args = parser.parse_args()

    # Define alphabets
    alphabets_dict = {
        'E': 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'Z': '♈♉♊♋♌♍♎♏♐♑♒♓',  # Zodiac symbols
        'G': 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ',  # Greek characters
        'A': 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي',  # Arabic characters
        'P': '☉☽☿♀♁♂♃♄♅♆♇',  # Planetary symbols
        'J': 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほ',  # Japanese Hiragana characters
        'S': '∀∂∃∅∇∈∉∋∏∑−∕∗∘√∝∞∠∧∨∩∪∫≈≠≡≤≥⊂⊃⊆⊇⊕⊗⊥⋅'  # Common scientific symbols
    }

    transformed_message = custom_rot_cipher(args.message, args.shift, args.mode, args.alphabets, alphabets_dict, args.null_symbol)
    print(transformed_message)

if __name__ == "__main__":
    main()

