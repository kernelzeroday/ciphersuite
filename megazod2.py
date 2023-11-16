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
        'Z2': '♈♉♊♋♌♍♎♏♐♑♒♓⛎',  # Zodiac Symbols (with Ophiuchus)
        'G': 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ',  # Greek Alphabet
        'GK': 'αβγδεζηθικλμνξοπρστυφχψω',  # Greek Alphabet (lowercase)
        'A': 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي',  # Arabic Alphabet
        'A2': 'ابتثجحخدذرزسشصضطظعغفقكلمنهويءآأؤإئ',  # Arabic Alphabet (with Hamza)
        'P': '☉☽☿♀♁♂♃♄♅♆♇',  # Planetary Symbols
        'P2': '☉☽☿♀♁♂♃♄♅♆♇☊☋',  # Planetary Symbols (with Nodes)
        'J': 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほ',  # Hiragana
        'S': '∀∂∃∅∇∈∉∋∏∑−∕∗∘√∝∞∠∧∨∩∪∫≈≠≡≤≥⊂⊃⊆⊇⊕⊗⊥⋅',  # Mathematical Symbols
        'S2': '∀∂∃∅∇∈∉∋∏∑−∕∗∘√∝∞∠∧∨∩∪∫≈≠≡≤≥⊂⊃⊆⊇⊕⊗⊥⋅⌈⌉⌊⌋〈〉',  # Mathematical Symbols (doubled)
        'H': '♥♦♣♠',  # Card Suits
        'H2': '♥♦♣♠♡♢♤♧',  # Card Suits (doubled)
        'C': '☯☮✝☪☸✡',  # Religious and Cultural Symbols
        'C2': '☯☮✝☪☸✡☥☦☧☨☩☪☫☬☭☮☯',  # Religious and Cultural Symbols (doubled)
        'M': '★☆☄☀☁☂☃☔',  # Meteorological Symbols
        'F': '🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🍍🥭🥥',  # Fruit Emojis
        'R': '🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐸🐵',  # Animal Emojis
        'O': '🚗🚕🚙🚌🚎🏎🚓🚑🚒🚐🛴🚲🛵🏍🚜',  # Vehicle Emojis
        'L': '🏁🚩🎌🏴🏳️🏳️‍🌈🏳️‍⚧️🇺🇳',  # Flag Emojis
        'L2': '🏁🚩🎌🏴🏳️🏳️‍🌈🏳️‍⚧️🇺🇳🇺🇸🇬🇧',  # Flag Emojis (doubled)
        'NAT': '🌲🌳🌴🌵🌷🌸🌹🌺🌻🌼💐',  # Nature and Flower Emojis
        'U': '🔥💧🌊💨🌍🌎🌏🌕🌖🌗🌘🌑🌒🌓🌔',  # Nature and Universe Emojis
        'I': '🔴🟠🟡🟢🔵🟣⚫⚪🟤🟥🟧🟨🟩🟦🟪',  # Colored Circle Emojis
        'T': '🀀🀁🀂🀃🀄🀅🀆🀇🀈🀉🀊🀋🀌🀍🀎🀏',  # Mahjong Tiles
        'D': '🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟',  # Clock Emojis
        'B': '🅰️🅱️🅾️🅿️🆎🆑🆒🆓🆔🆕🆖🆗🆘🆙🆚🈁🈂️🈷️🈶🈯🉐🈹',  # Enclosed Alphanumerics
        'B2': '🅰️🅱️🆎🆑🅾️🆘🆔🆚🈁🈂️🈷️🈶🈯🉐🈹',  # Enclosed Alphanumerics
        'N': '🔢🔣🔤🅿️🆖🆗🆙🆒🆕🆓🆔🆓🆙🆗🆖🔤🔣🔢',  # Enclosed Alphanumerics (doubled)
        'K': 'คงจชซฌญฎฏฐฑฒณดตถทธนบปผพภมยรลวศษสหฬอ',  # Thai Alphabet
        'K2': 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผพภมยรลวศษสหฬอฮ',  # Thai Alphabet (with ก)
        'Q': '🀄🎴🃏🂡🂱🃁🃑🂢🂲🃂🃒🂣🂳🃃🃓',  # Playing Cards
        'W': '🌑🌒🌓🌔🌕🌖🌗🌘',  # Moon Phases
        'RU': 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',  # Russian Alphabet
        'CH': '中國哲學書電子化計劃简体中文繁體中文',  # Simplified & Traditional Chinese Characters
        'KO': '가나다라마바사아자차카타파하',  # Korean Hangul
        'KO2': '가나다라마바사아자차카타파하각갂갃간갅갆갇갈갉갊갋갌갍갎갏감',  # Korean Hangul (doubled)
        'HI': 'अआइईउऊऋएऐओऔकखगघङचछ',  # Hindi Devanagari Script
        'HI2': 'अआइईउऊऋएऐओऔकखगघङचछजझ',  # Hindi Devanagari Script with J
        'HI3': 'अआइईउऊऋएऐओऔकखगघङचछजझञट',  # Hindi Devanagari Script with J and T
        'CY': '☀☁☂☃☄⚡❄⛄⚠️⚔️☠️⚓⚒️⚙️⚗️⚖️',  # Symbols (Cyclical, Weather, Warnings, Tools)
        'MU': '🎵🎶🎼🎷🎸🎹🎺🎻🥁🪘🪕🪗🪒🎤🎧',  # Music and Instruments Emojis
        'SP': '⚽🏀🏈⚾🎾🏐🏉🎱🏓🏸🥊🥋🥏🥌🛹',  # Sports Emojis
        'TE': '📱📲💻🖥️🖨️🕹️🖱️🖲️🧮⌨️',  # Technology and Electronics Emojis
        'NA': '🌲🌳🌴🌵🌷🌸🌹🌺🌻🌼💐',  # Nature and Flower Emojis
        'AR': '🏛️🏰🕌🕍🕋⛩️🗿🏗️🏭🏢',  # Architecture and Landmark Emojis
        'AC': '🧩🎨🎭🎪🎤🎬🎰🚀🛸🧲',  # Activities and Entertainment Emojis
        'SN': '🔔🔕🔈🔉🔊📢📣📯🔇🎼',  # Sound and Notification Emojis
        'SY': '✂️🔒🔑🔨🪓🔧🔩🧰🧲🔗',  # Symbolic Objects
        'FO': '🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🍍🥭🥥🥝🍅🍆🥑🥦🥬🥒🌶️🌽🥕🧄🧅🥔🍠🥐🥯🍞🥖🥨🧀🥚🍳🧈🥞🧇🥓🥩🍗🍖🦴🌭🍔🍟🍕🥪🥙🧆🌮🌯🥗🥘🥫🍝🍜🍲🍛🍣🍱🥟🦪🍤🍙🍚🍘🍥🥠🥮🍢🍡🍧🍨🍦🥧🧁🍰🎂🍮🍭🍬🍫🍿🍩🍪🌰🥜🍯🥛🍼☕🍵🧃🥤🧋🍶🍺🍻🥂🍷🥃🍸🍹🍾🥄🍴🍽️🥣🥡🥢',  # Food and Drink Emojis
        'TR': '🚗🚕🚙🚌🚎🏎️🚓🚑🚒🚐🛴🚲🛵🏍️🚜🚚🚛🚔🚍🚘🚖🚡🚠🚟🚃🚋🚝🚄🚅🚈🚞🚂🚆🚇🚊🚉🚁🛩️✈️🛫🛬🚀🛰️🚤⛵🛶⚓🚢🚧⛽🚏🚦🚥🗺️🗿🗽🗼🏰🏯🏟️🎡🎢🎠⛲🏖️🏝️🏜️🌋⛰️🏔️🗻🏕️⛺🏠🏡🏘️🏚️🏗️🏭🏢🏬🏣🏤🏥🏦🏨🏪🏫🏩💒🏛️⛪🕌🕍🕋⛩️🛤️🛣️🗾🎑🏞️🌅🌄🌠🎇🎆🌇🌆🏙️🌃🌌🌉🌁',  # Travel and Transport Emojis
        'PL': '🏛️🏰🕌🕍🕋⛩️🗿🏗️🏭🏢🏠🏡🏘️🏚️🏬🏣🏤🏥🏦🏨🏪🏫🏩💒🏛️⛪🕌🕍🕋⛩️🛤️🛣️🗾🎑🏞️🌅🌄🌠🎇🎆🌇🌆🏙️🌃🌌🌉🌁',  # Place Emojis
        'OB': '⌚️📱📲💻⌨️🖥️🖨️🖱️🖲️🕹️🗜️💽💾💿📀📼📷📸📹🎥📽️🎞️📞☎️📟📠📺📻🎙️🎚️🎛️⏱️⏲️⏰🕰️⌛️⏳📡🔋🔌💡🔦🕯️🪔🧯🛢️💸💵💴💶💷💰💳💎⚖️🧰🔧🔨⚒️🛠️⛏️🔩⚙️🧱⛓️🧲🔫💣🧨🪓🔪🗡️⚔️🛡️🚬⚰️⚱️🏺🔮📿💈⚗️🔭🔬🕳️💊💉🩸🩹🩺🌡️🧬', # Object Emojis
        'MA': '𝟬𝟭𝟮𝟯𝟰𝟱𝟳𝟴𝟵𝟭𝟬𝟭𝟮𝟯',  # Mathematical Numbers
        'MS': '𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙',  # Mathematical Sans-Serif Alphabet
        'MS2': '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳',  # Mathematical Sans-Serif Alphabet (lowercase)
        'MS3': '𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁',  # Mathematical Sans-Serif Alphabet (italic)
        'AS': '🚀🛸🛰️🔭🪐🌠🌌🌟🌜🌛',  # Astronomical Symbols and Emojis
        'AS2': '🚀🛸🛰️🔭🪐🌠🌌🌟🌜🌛🌝🌞🌙🌚🌕🌖🌗🌘🌑🌒🌓🌔',  # Astronomical Symbols and Emojis (doubled)
        'AS3': '🚀🛸🛰️🔭🪐🌠🌌🌟🌜🌛🌝🌞🌙🌚🌕🌖🌗🌘🌑🌒🌓🌔🌙🌚🌕🌖🌗🌘🌑🌒🌓🌔',  # Astronomical Symbols and Emojis (tripled)
        'ASC': '!@#$%^&*()_+-=[]{}|;:",.<>/?',  # ASCII Special Characters
        'ASC2': '!@#$%^&*()_+-=[]{}|;:",.<>/?`~',  # ASCII Special Characters with Tilde
        'ASC3': '!@#$%^&*()_+-=[]{}|;:",.<>/?`~\'',  # ASCII Special Characters with Tilde and Apostrophe
        'ASC4': '!@#$%^&*()_+-=[]{}|;:",.<>/?`~\'\\',  # ASCII Special Characters with Tilde, Apostrophe, and Backslash
        'ASC5': '!@#$%^&*()_+-=[]{}|;:",.<>/?`~\'\\\"',  # ASCII Special Characters with Tilde, Apostrophe, Backslash, and Double Quote
        'ASC6': '!@#$%^&*()_+-=[]{}|;:",.<>/?`~\'\\\" ',  # ASCII Special Characters with Tilde, Apostrophe, Backslash, Double Quote, and Space
        'EN1': 'ABCDEFGHJKLMNOPQRSTUVWXYZ',  # English Alphabet without I and M
        'EN2': 'NPQRSTUVWXYZabcdefghijklm',  # Second Half of English Alphabet Transposed
        'REV': 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA',  # Reversed English Alphabet
        'REV2': 'mlkjihgfedcbazyxwvutsrqponMLKJIHGFEDCBAZYXWVUTSRQPON',  # Second Half of Reversed English Alphabet Transposed
        'RU2': 'ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЕДГВБА',  # Reversed Russian Alphabet
        'RU3': 'ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЕДГВБАяюэьыъщшчцхфутсрпонмлкйизжедгвба',  # Reversed Russian Alphabet (lowercase)
        'RU4': 'ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЕДГВБАяюэьыъщшчцхфутсрпонмлкйизжедгвбаё',  # Reversed Russian Alphabet (lowercase) with Ё
        'ER': 'АBCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюя',  # English Transposed on Russian
        'N1': '0123456789',  # Numbers
        'N2': '9876543210',  # Reversed Numbers
        'HR': '♨❤☀☆☂☻♞☯☭☢⚡⚙☏☔⚖♔♕♖♗♘♙♚♝♞♟',  # Various Symbols
        'HR2': '♨❤☀☆☂☻♞☯☭☢⚡⚙☏☔⚖♔♕♖♗♘♙♚♝♞♟⚀⚁⚂⚃⚄⚅',  # Various Symbols with Dice
        'FR': '😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😏😒😞😔😟',  # Facial Reaction Emojis
        'FR2': '😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😏😒😞😔😟😕🙁☹️😣😖😫😩😢😭😤😠😡🤬🤯😳😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾',  # Facial Reaction Emojis
        'SH': '♠♥♦♣♤♡♢♧',  # Card Suits with Alternatives
        'SH2': '♠♥♦♣♤♡♢♧♤♡♢♧',  # Card Suits with Alternatives (doubled)
        'BR': '(){}[]<>',  # Brackets
        'ARW': '←↑→↓↔↕↖↗↘↙⬆⬇⬅➡⬅➡⬆⬇↩↪',  # Arrows
        'ARW2': '←↑→↓↔↕↖↗↘↙⬆⬇⬅➡⬅➡⬆⬇↩↪↫↬↭↰↱↲↳↴↵↶↷↺↻⇄⇅⇆⇇⇈⇉⇊⇋⇌⇍⇎⇏⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙⇚⇛⇜⇝⇞⇟⇠⇡⇢⇣⇤⇥⇦⇧⇨⇩⇪⇫⇬⇭⇮⇯⇰⇱⇲⇳⇴⇵⇶⇷⇸⇹⇺⇻⇼⇽⇾⇿',  # Arrows (doubled)
        'MAT': '+−×÷=≠≈<>≤≥∑∏√∛∜',  # Mathematical Operators
        'MIS': '⌚⌛⏰⏳⏲️⏱️⏴️⏵️⏶️⏷️⏸️⏹️⏺️⏭️⏮️⏩⏪⏫⏬⏯️⏸️⏹️⏺️⏏️⏫⏬⏭️⏮️⏯️⏰⏱️⏲️⏳⌛⌚',  # Miscellaneous Symbols
        'CLK': '🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦',  # Clock Faces
        'SQ': '🔲🔳⬛⬜◼◻◾◽▪▫',  # Square Shapes
        'TRI': '▲▼◀▶△▽◁▷▴▾◅▻',  # Triangle Shapes
        'CIR': '⭕🔴🔵⚪⚫🟠🟡🟢🔺🔻',  # Circle Shapes
        'STR': '✶✹✸✷✵✴✳✼✻✽',  # Star Shapes
        'MNY': '💲💰💸💵💴💶💷💳💹💱',  # Money and Currency Emojis
        'VEH': '🚗🚕🚙🚚🚛🚜🚲🚏🛤️🚦',  # Vehicle and Traffic Emojis
        'FOO': '🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈',  # Food Emojis
        'DRK': '🍺🍻🥂🥃🍷🍸🍹🍾🍶🥛',  # Drink Emojis
        'ACT': '🎭🎬🎤🎧🎼🎹🎷🎺🎸🥁',  # Activity and Music Emojis
        'TRV': '✈️🚄🚅🚆🚇🚈🚉🚊🚋🚌',  # Travel and Transport Emojis
        'PLC': '🏠🏡🏢🏣🏤🏥🏦🏨🏩🏪',  # Place Emojis
        'OBJ': '⌚️📱📲💻⌨️🖥️🖨️🖱️🖲️🕹️',  # Object Emojis
        'SYM': '💟✅🆚🆎🅾️🔠🔡🔢🔣🔤',  # Symbol Emojis
        'FLG': '🏁🚩🎌🏴🏳️🏳️‍🌈🏳️‍⚧️🇺🇳🇺🇸🇬🇧',  # Flag Emojis
        'BIR': '🐦🐧🐤🐥🐣🦆🦢🦜🦩🦚',  # Bird Emojis
        'ANM': '🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯',  # Animal Emojis
        'PLT': '🌵🌴🌳🌲🌱🌿☘️🍀🎍🎋',  # Plant Emojis
        'SEA': '🐳🐬🐟🐠🐡🦈🐙🐚🦀🦞',  # Sea Life Emojis
        'SKY': '🌞🌝🌛🌜🌚🌕🌖🌗🌘🌑',  # Sky and Weather Emojis
        'BOK': '📚📖📕📗📘📙📔📒📓📑',  # Book Emojis
        'HEA': '❤️🧡💛💚💙💜🤎🖤🤍💔',  # Heart Emojis
        'HEA2': '❤️🧡💛💚💙💜🤎🖤🤍💔💕💞💓💗💖💘💝',  # Heart Emojis (doubled)
        'HND': '👍👎👌👊✊✌️🤞🤟🤘🤙',  # Hand Emojis
        'ZK': '⊛⊕⊖⊗⊘⊙⊚⊛⊜⊝',  # Zodiak Killer Symbols
        'ZK2': '⊛⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡',  # Zodiak Killer Symbols with Squares
        'FS': '🔍🔐🔓🔏🔎🔑🔒🔔🔕🔖',  # Famous Cipher Symbols
        'HE': 'אבגדהוזחטיכלמנסעפצקרשת',  # Hebrew Alphabet
        'HE2': 'אבגדהוזחטיכלמנסעפצקרשתךםןףץ',  # Hebrew Alphabet with Final Forms
        'HE3': 'אבגדהוזחטיכלמנסעפצקרשתךםןףץ׳״',  # Hebrew Alphabet with Final Forms and Punctuation
        'HE4': 'אבגדהוזחטיכלמנסעפצקרשתךםןףץ׳״ׇ',  # Hebrew Alphabet with Final Forms, Punctuation, and Cantillation Marks
        'PH': '𐤀𐤁𐤂𐤃𐤄𐤅𐤆𐤇𐤈𐤉𐤊𐤋𐤌𐤍𐤎𐤏𐤐𐤑𐤒𐤓𐤔𐤕𐤖𐤗𐤘𐤙𐤚𐤛𐤜𐤝𐤞𐤟𐤠𐤡𐤢𐤣𐤤𐤥𐤦𐤧𐤨𐤩𐤪𐤫𐤬𐤭𐤮𐤯𐤰𐤱𐤲𐤳𐤴𐤵𐤶𐤷𐤸𐤹𐤺𐤻𐤼𐤽𐤾𐤿',  # Phoenician Alphabet
        'R': 'ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛋᛏᛒᛖᛗᛚᛜᛞᛟᚪᚫᚣᛡᛠ',  # Elder Futhark
        'R2': 'ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛋᛏᛒᛖᛗᛚᛜᛞᛟᚪᚫᚣᛡᛠᛤᛥᛦ',  # Elder Futhark (with ᛤᛥᛦ)
        'R3': 'ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛋᛏᛒᛖᛗᛚᛜᛞᛟᚪᚫᚣᛡᛠᛤᛥᛦᛧᛨᛩᛪ᛫᛬᛭ᛮᛯ',  # Elder Futhark (with ᛤᛥᛦ and ᛧᛨᛩᛪ᛫᛬᛭ᛮᛯ)
        'R4': 'ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛋᛏᛒᛖᛗᛚᛜᛞᛟᚪᚫᚣᛡᛠᛤᛥᛦᛧᛨᛩᛪ᛫᛬᛭ᛮᛯᛰ',  # Elder Futhark (with ᛤᛥᛦ, ᛧᛨᛩᛪ᛫᛬᛭ᛮᛯ, and ᛰ)
        # obscure alphabets
        'O1': '⚀⚁⚂⚃⚄⚅',  # Dice
        'O2': '⚀⚁⚂⚃⚄⚅⚀⚁⚂⚃⚄⚅',  # Dice (doubled)
        # egypian hieroglyphs
        'E1': '𓀀𓀁𓀂𓀃𓀄𓀅𓀆𓀇𓀈𓀉𓀊𓀋𓀌𓀍𓀎𓀏𓀐𓀑𓀒𓀓𓀔𓀕𓀖𓀗𓀘𓀙𓀚𓀛𓀜𓀝𓀞𓀟𓀠𓀡𓀢𓀣𓀤𓀥𓀦𓀧𓀨𓀩𓀪𓀫𓀬𓀭𓀮𓀯𓀰𓀱𓀲𓀳𓀴𓀵𓀶𓀷𓀸𓀹𓀺𓀻𓀼𓀽𓀾𓀿𓁀𓁁𓁂𓁃𓁄𓁅𓁆𓁇𓁈𓁉𓁊𓁋𓁌𓁍𓁎𓁏𓁐𓁑𓁒𓁓𓁔𓁕𓁖𓁗𓁘𓁙𓁚𓁛𓁜𓁝𓁞𓁟𓁠𓁡𓁢𓁣𓁤𓁥𓁦𓁧𓁨𓁩𓁪𓁫𓁬𓁭𓁮𓁯𓁰𓁱𓁲𓁳𓁴𓁵𓁶𓁷𓁸𓁹𓁺',
        # sumerian cuneiform
        'CUN': '𒀸𒀼𒁋𒂊𒂞𒃶𒄒𒅗𒆳𒇇𒈠𒉌𒊏𒋗𒌁',
        




    }

    transformed_message = custom_rot_cipher(args.message, args.shift, args.mode, args.alphabets, alphabets_dict, args.nulls)
    print(transformed_message)

if __name__ == "__main__":
    main()
