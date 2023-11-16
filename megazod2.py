import argparse

def create_mapping(english_alphabet, selected_alphabets, shift, nulls):
    mapping = {}
    reverse_mapping = {}
    extended_alphabet = [char for char in selected_alphabets if char not in nulls]
    collision_warnings = []

    if len(extended_alphabet) == 0:
        return {}, {}, []  # Return empty mappings and warnings if extended_alphabet is empty

    shift %= len(extended_alphabet)

    used_cipher_chars = set()

    # Create mapping for encoding, avoiding collision-causing characters
    for i, char in enumerate(english_alphabet):
        if char in nulls:
            continue  # Skip null characters

        shifted_index = (i + shift) % len(extended_alphabet)
        cipher_char = extended_alphabet[shifted_index]

        # Add a check to prevent infinite loop
        attempts = 0
        while cipher_char in used_cipher_chars and attempts < len(extended_alphabet):
            shifted_index = (shifted_index + 1) % len(extended_alphabet)
            cipher_char = extended_alphabet[shifted_index]
            attempts += 1

        if attempts == len(extended_alphabet):
            collision_warnings.append((char, cipher_char))
        else:
            mapping[char] = cipher_char
            reverse_mapping[cipher_char] = char
            used_cipher_chars.add(cipher_char)

    return mapping, reverse_mapping, collision_warnings



def custom_rot_cipher(input_str, shift, mode, alphabets, alphabets_dict, nulls):
    english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    
    selected_alphabets = ''.join(alphabets_dict[char] for char in alphabets.split(',') if char in alphabets_dict)

    if not selected_alphabets:
        raise ValueError("Selected alphabets string is empty. Please check the --alphabets argument.")

    mapping, reverse_mapping, collision_warnings = create_mapping(english_alphabet, selected_alphabets, shift, nulls)

    result = ''
    possible_results = []

    for char in input_str:
        if mode == 'encode':
            if char in nulls:
                result += char  # Leave null characters unchanged in encoding
            else:
                result += mapping.get(char, char)  # Use mapped char or original char if not in mapping
        elif mode == 'decode':
            if char not in nulls:
                result += reverse_mapping.get(char, char)  # Use original char if not in reverse mapping
                if char in collision_warnings:
                    possible_results.append([reverse_mapping.get(c, c) for c in input_str])

    if possible_results:
        return possible_results
    else:
        return result

def main():
    parser = argparse.ArgumentParser(description='Custom ROT cipher with multiple selectable alphabets for encoding and decoding English text.')
    parser.add_argument('mode', type=str, choices=['encode', 'decode'], help='Mode of operation: encode or decode.')
    parser.add_argument('shift', type=int, help='Shift value for the cipher.')
    parser.add_argument('message', type=str, help='Message to encode or decode.')
    # Updated help description for the --alphabets argument
    parser.add_argument('--alphabets', type=str, default='E', help='Comma-separated list of alphabets to use (e.g., "E,Z,G,RU"). Available options include E (English), Z (Zodiac), P (Planetary), G (Greek), A (Arabic), J (Japanese), S (Scientific), RU (Russian), CH (Chinese), KO (Korean), and more.')
    parser.add_argument('--nulls', type=str, default='', help='String of valid null characters to be ignored in the cipher.')

    args = parser.parse_args()

    # Define alphabets
    # Seed thought: Expand alphabets_dict with a wide variety of symbols and characters
    alphabets_dict = {
        'E': 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',  # English Alphabet
        'Z': '♈♉♊♋♌♍♎♏♐♑♒♓',  # Zodiac Symbols
        'G': 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ',  # Greek Alphabet
        'A': 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي',  # Arabic Alphabet
        'P': '☉☽☿♀♁♂♃♄♅♆♇',  # Planetary Symbols
        'J': 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほ',  # Hiragana
        'S': '∀∂∃∅∇∈∉∋∏∑−∕∗∘√∝∞∠∧∨∩∪∫≈≠≡≤≥⊂⊃⊆⊇⊕⊗⊥⋅',  # Mathematical Symbols
        'H': '♥♦♣♠',  # Card Suits
        'C': '☯☮✝☪☸✡',  # Religious and Cultural Symbols
        'M': '★☆☄☀☁☂☃☔',  # Meteorological Symbols
        'F': '🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🍍🥭🥥',  # Fruit Emojis
        'R': '🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐸🐵',  # Animal Emojis
        'O': '🚗🚕🚙🚌🚎🏎🚓🚑🚒🚐🛴🚲🛵🏍🚜',  # Vehicle Emojis
        'L': '🏁🚩🎌🏴🏳️🏳️‍🌈🏳️‍⚧️🇺🇳',  # Flag Emojis
        'U': '🔥💧🌊💨🌍🌎🌏🌕🌖🌗🌘🌑🌒🌓🌔',  # Nature and Universe Emojis
        'I': '🔴🟠🟡🟢🔵🟣⚫⚪🟤🟥🟧🟨🟩🟦🟪',  # Colored Circle Emojis
        'T': '🀀🀁🀂🀃🀄🀅🀆🀇🀈🀉🀊🀋🀌🀍🀎🀏',  # Mahjong Tiles
        'D': '🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟',  # Clock Emojis
        'B': '🅰️🅱️🆎🆑🅾️🆘🆔🆚🈁🈂️🈷️🈶🈯🉐🈹',  # Enclosed Alphanumerics
        'K': 'คงจชซฌญฎฏฐฑฒณดตถทธนบปผพภมยรลวศษสหฬอ',  # Thai Alphabet
        'Q': '🀄🎴🃏🂡🂱🃁🃑🂢🂲🃂🃒🂣🂳🃃🃓',  # Playing Cards
        'RU': 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',  # Russian Alphabet
        'CH': '中國哲學書電子化計劃简体中文繁體中文',  # Simplified & Traditional Chinese Characters
        'KO': '가나다라마바사아자차카타파하',  # Korean Hangul
        'HI': 'अआइईउऊऋएऐओऔकखगघङचछ',  # Hindi Devanagari Script
        'CY': '☀☁☂☃☄⚡❄⛄⚠️⚔️☠️⚓⚒️⚙️⚗️⚖️',  # Symbols (Cyclical, Weather, Warnings, Tools)
        'MU': '🎵🎶🎼🎷🎸🎹🎺🎻🥁🪘🪕🪗🪒🎤🎧',  # Music and Instruments Emojis
        'SP': '⚽🏀🏈⚾🎾🏐🏉🎱🏓🏸🥊🥋🥏🥌🛹',  # Sports Emojis
        'TE': '📱📲💻🖥️🖨️🕹️🖱️🖲️🧮⌨️',  # Technology and Electronics Emojis
        'NA': '🌲🌳🌴🌵🌷🌸🌹🌺🌻🌼💐',  # Nature and Flower Emojis
        'AR': '🏛️🏰🕌🕍🕋⛩️🗿🏗️🏭🏢',  # Architecture and Landmark Emojis
        'AC': '🧩🎨🎭🎪🎤🎬🎰🚀🛸🧲',  # Activities and Entertainment Emojis
        'SN': '🔔🔕🔈🔉🔊📢📣📯🔇🎼',  # Sound and Notification Emojis
        'SY': '✂️🔒🔑🔨🪓🔧🔩🧰🧲🔗',  # Symbolic Objects
        'MA': '𝟬𝟭𝟮𝟯𝟰𝟱𝟳𝟴𝟵𝟭𝟬𝟭𝟮𝟯',  # Mathematical Numbers
        'AS': '🚀🛸🛰️🔭🪐🌠🌌🌟🌜🌛',  # Astronomical Symbols and Emojis
        'ASC': '!@#$%^&*()_+-=[]{}|;:",.<>/?',  # ASCII Special Characters
        'EN1': 'ABCDEFGHJKLMNOPQRSTUVWXYZ',  # English Alphabet without I and M
        'EN2': 'NPQRSTUVWXYZabcdefghijklm',  # Second Half of English Alphabet Transposed
        'REV': 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA',  # Reversed English Alphabet
        'ER': 'АBCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюя',  # English Transposed on Russian
        'N1': '0123456789',  # Numbers
        'N2': '9876543210',  # Reversed Numbers
        'HR': '♨❤☀☆☂☻♞☯☭☢⚡⚙☏☔⚖♔♕♖♗♘♙♚♝♞♟',  # Various Symbols
        'FR': '😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😏😒😞😔😟',  # Facial Reaction Emojis
        'SH': '♠♥♦♣♤♡♢♧',  # Card Suits with Alternatives
        'BR': '(){}[]<>',  # Brackets
        'ARW': '←↑→↓↔↕↖↗↘↙⬆⬇⬅➡⬅➡⬆⬇↩↪',  # Arrows
        'MAT': '+−×÷=≠≈<>≤≥∑∏√∛∜',  # Mathematical Operators
        'CLK': '🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦',  # Clock Faces
        'SQ': '🔲🔳⬛⬜◼◻◾◽▪▫',  # Square Shapes
        'TRI': '▲▼◀▶△▽◁▷▴▾◅▻',  # Triangle Shapes
        'CIR': '⭕🔴🔵⚪⚫🟠🟡🟢🔺🔻',  # Circle Shapes
        'STR': '✶✹✸✷✵✴✳✼✻✽',  # Star Shapes
        'MNY': '💲💰💸💵💴💶💷💳💹💱',  # Money and Currency Emojis
        'VEH': '🚗🚕🚙🚚🚛🚜🚲🚏🛤️🚦',  # Vehicle and Traffic Emojis


    }

    transformed_message = custom_rot_cipher(args.message, args.shift, args.mode, args.alphabets, alphabets_dict, args.nulls)
    print(transformed_message)

if __name__ == "__main__":
    main()
