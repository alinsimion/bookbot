def count_chars(text):
    char_dict = {}
    for char in text:
        if char.isalpha() == False:
            continue
        sanitized_char = char.lower()
        char_dict[sanitized_char] = char_dict.get(sanitized_char, 0) + 1

    return char_dict

def main():
    text = ""
    with open("books/frankenstein.txt", "r") as f:
        text = f.read()
        # print(text)
    print("The text has ", len(text.split()), " words")
    
    char_dict = count_chars(text)
    for char, count in char_dict.items():
        print(f"The {char} character was found {count} time")


main()