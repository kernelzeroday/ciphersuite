import argparse
import random

def find_missing_characters(input_string, filter_string):
    # Seed Thought: Expand ASCII range to include lowercase and numbers
    all_characters = set(chr(i) for i in range(65, 91)) | set(chr(i) for i in range(97, 123)) | set(chr(i) for i in range(48, 58))

    input_characters = set(input_string)
    missing_characters = all_characters - input_characters

    if filter_string:
        filter_characters = set(filter_string)
        missing_characters -= filter_characters

    return missing_characters

def auto_inject_characters(input_string, missing_characters):
    # Convert the set to a list for random sampling
    missing_characters_list = list(missing_characters)

    # Randomly inject missing characters into the input string
    for char in random.sample(missing_characters_list, k=min(len(missing_characters_list), 3)): # Inject up to 3 characters
        insert_position = random.randint(0, len(input_string))
        input_string = input_string[:insert_position] + char + input_string[insert_position:]

    return input_string


def main():
    parser = argparse.ArgumentParser(description='Find missing characters in a string and optionally inject them.')
    parser.add_argument('-m', '--message', required=True, type=str, help='The string to analyze.')
    parser.add_argument('--filter', type=str, help='String of characters to exclude from the output.', default='')
    parser.add_argument('--auto-inject', action='store_true', help='Automatically inject some missing characters into the message.')

    args = parser.parse_args()
    missing_characters = find_missing_characters(args.message, args.filter)

    if args.auto_inject:
        new_message = auto_inject_characters(args.message, missing_characters)
        used_nulls = set(new_message) - set(args.message)
        print(f"Nulls used: {''.join(sorted(used_nulls))}")
        print(f"Null padded string: {new_message}")
    else:
        print(''.join(sorted(missing_characters)))

if __name__ == "__main__":
    main()
