from stats import get_num_words, report_sort

chars = report_sort()
words = get_num_words()

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {words} total words")
print("--------- Character Count -------")
for char_data in chars:
    print(f"{char_data['char']}: {char_data['count']}")
print("============= END ===============")