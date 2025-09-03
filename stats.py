def count_words(book_text):
    word_count = len(book_text.split())
    return word_count

def count_characters(text):
    characters = {}
    
    for letter in text.lower():
        if letter in characters:
            count = characters[letter]
            characters[letter]=count + 1
        else:
            characters[letter]=1
    return characters