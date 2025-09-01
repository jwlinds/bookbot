def get_num_words(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def get_char_counts(file_contents):
    characters = file_contents.lower()
    char_count ={}
    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(char_count):
    return char_count["num"]

def get_sorted_chars(char_count):
    sorted_chars = []
    for letter in char_count:
        count = char_count[letter]
        sorted_chars.append({"char":letter, "num":count})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

# def print_sorted_chars(sorted_chars):
#     for pair in sorted_chars:
#         print(f"{pair["char"]}: {pair["num"]}")