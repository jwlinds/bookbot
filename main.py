
from stats import get_num_words, get_char_counts, get_sorted_chars
# from stats import print_sorted_chars

def get_book_text(path_to_file):
   with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main(path_to_file):
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_char_list = get_sorted_chars(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------") 
    for pair in sorted_char_list:
        print(f"{pair['char']}: {pair['num']}")

main("books/frankenstein.txt")
