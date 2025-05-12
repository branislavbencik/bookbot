
from stats import get_num_words
from stats import get_letter_count
from stats import sort_chars
import sys

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    num_chars = get_letter_count(text)
    sorted = sort_chars(num_chars)

    print("============ BOOKBOT ============ ")
    print("Analyzing book found at books/frankenstein.txt... ")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
   
    for item in sorted:
        print(f"{item['char']}: {item['count']}")
        
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


main()