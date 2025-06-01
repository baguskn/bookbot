from stats import get_num_words, get_chars_dict, get_sorted_alpha_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_alpha_dict = get_sorted_alpha_dict(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_alpha_dict:
        print(f"{char}: {sorted_alpha_dict[char]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
