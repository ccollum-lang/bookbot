def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count


def get_chars_dict(text):
    chars = {}
    
    for letter in text.lower():
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars


def sort_on(dict):
    return dict["num"]


def sortd_chars_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char":char, "num":num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list