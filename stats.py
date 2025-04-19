def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def get_num_words():
    book_text = get_book_text("books/frankenstein.txt")
    words = book_text.split()
    word_count = len(words)
    print(f"{word_count} words found in the document")



def get_num_characters():
    chars = {}
    book_text = get_book_text("books/frankenstein.txt")
    for char in book_text.lower():
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars



