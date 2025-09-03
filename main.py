def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def count_words(book_text):
    word_count = len(book_text.split())
    return word_count


def main():
    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")


main()
    