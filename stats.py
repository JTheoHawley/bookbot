def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def get_num_words(text):
    words = text.split()
    word_count = len(words)
    return word_count



def get_num_characters(text):
    chars = {}
    for char in text.lower():
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars

def sort_dict(dict):
    return dict["count"]

def get_sort(chars):
    chars_dict = []
    for character, count in chars.items():
        if character.isalpha():
            chars_dict.append({"char":character, "count": count})

    chars_dict.sort(reverse=True, key=sort_dict)
    return chars_dict

def report_sort(text):
    chars = get_num_characters(text)
    return get_sort(chars)


