def main():
    with open('books/frankenstein.txt', 'r') as file:
        file_contents = file.read()
    print(file_contents)
    word_count = count(file_contents)
    print(f"The book contains {word_count} words.")
    print(f"The book contains {count_chars(file_contents)} characters.")

def count(file_contents):
    return len(file_contents.split())

def count_chars(file_contents):
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    text = file_contents.lower()

    total_chars = 0
    char_count = {}

    for c in text:
        if c in characters:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
    
    for char in char_count:
        total_chars += char_count[char]
        print(f"the {char} character was found {char_count[char]} times.")
    
    return total_chars

main()