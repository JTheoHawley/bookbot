import sys
from stats import get_num_words, report_sort, get_book_text

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

text = get_book_text(sys.argv[1])
chars = report_sort(text)
words = get_num_words(text)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {words} total words")
print("--------- Character Count -------")
for char_data in chars:
    print(f"{char_data['char']}: {char_data['count']}")
print("============= END ===============")