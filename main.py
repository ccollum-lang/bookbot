def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    print(text)

main()
    