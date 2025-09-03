from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    print(count_characters(text))


main()
    