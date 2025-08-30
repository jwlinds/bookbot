def get_num_words(file_contents):
    word_list = file_contents.split()
    return f"{len(word_list)} words found in the document"

def get_char_counts(file_contents):
    characters = file_contents.lower()
    char_count ={}
    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
