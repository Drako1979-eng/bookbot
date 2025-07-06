# ============= INITIAL FUNCTION IMPORTS ==================

import sys
# import stat functions from stats.py
from stats import count_words
from stats import count_chars
from stats import letter_sort

# =================== EXTRA FUNCTIONS =====================

# function which reads the contents of a file and outputs it to a string
def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

# ==================== MAIN PROGRAM =======================

book_adress = None
arg_length = len(sys.argv)
# Read command line arguments:
if arg_length == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_adress = sys.argv[1]
    # Downloads the text from frankenstein.txt
    text = get_book_text(book_adress)

    # Print the book stats:
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_adress}...")

    print("--------- Word Count ---------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")

    print("------- Character Count -------")
    letter_count = count_chars(text)
    #print(letter_count)
    letter_list = letter_sort(letter_count)
    for item in letter_list:
        print(f"{item['name']}: {item['num']}")

    print("=========== END ===========")



    
