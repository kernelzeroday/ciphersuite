import argparse

def create_mapping(english_alphabet, selected_alphabets, shift, nulls):
    mapping = {}
    extended_alphabet = [char for char in selected_alphabets if char not in nulls]
    shift %= len(extended_alphabet)

    # Create mapping for encoding
    for i, char in enumerate(english_alphabet):
        if char not in nulls:
            shifted_index = (i + shift) % len(extended_alphabet)
            mapping[char] = extended_alphabet[shifted_index]

    # Create reverse mapping for decoding
    reverse_mapping = {v: k for k, v in mapping.items()}

    return mapping, reverse_mapping

def custom_rot_cipher(input_str, shift, mode, alphabets, alphabets_dict, nulls):
    english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    selected_alphabets = ''.join(alphabets_dict[char] for char in alphabets if char in alphabets_dict)

    mapping, reverse_mapping = create_mapping(english_alphabet, selected_alphabets, shift, nulls)

    result = ''

    for char in input_str:
        if mode == 'encode':
            if char in nulls:
                result += char  # Leave null characters unchanged in encoding
            else:
                result += mapping.get(char, char)  # Use mapped char or original char if not in mapping
        elif mode == 'decode':
            if char not in nulls:
                result += reverse_mapping.get(char, char)  # Use original char if not in reverse mapping

    return result

def main():
    parser = argparse.ArgumentParser(description='Custom ROT cipher with multiple selectable alphabets for encoding and decoding English text.')
    parser.add_argument('mode', type=str, choices=['encode', 'decode'], help='Mode of operation: encode or decode.')
    parser.add_argument('shift', type=int, help='Shift value for the cipher.')
    parser.add_argument('message', type=str, help='Message to encode or decode.')
    parser.add_argument('--alphabets', type=str, default='E', help='Alphabets to use: E for English, Z for Zodiac, P for Planetary, G for Greek, A for Arabic, J for Japanese, S for Scientific.')
    parser.add_argument('--nulls', type=str, default='', help='String of valid null characters to be ignored in the cipher.')

    args = parser.parse_args()

    # Define alphabets
    alphabets_dict = {
        'E': 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'Z': '♈♉♊♋♌♍♎♏♐♑♒♓',
        'G': 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ',
        'A': 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي',
        'P': '☉☽☿♀♁♂♃♄♅♆♇',
        'J': 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほ',
        'S': '∀∂∃∅∇∈∉∋∏∑−∕∗∘√∝∞∠∧∨∩∪∫≈≠≡≤≥⊂⊃⊆⊇⊕⊗⊥⋅'
    }

    transformed_message = custom_rot_cipher(args.message, args.shift, args.mode, args.alphabets, alphabets_dict, args.nulls)
    print(transformed_message)

if __name__ == "__main__":
    main()
