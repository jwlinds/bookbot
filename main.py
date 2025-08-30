
from stats import get_num_words, get_char_counts


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main(path_to_file):
    print(get_num_words(get_book_text(path_to_file)))
    print(get_char_counts(get_book_text(path_to_file)))    

main("./books/frankenstein.txt")
