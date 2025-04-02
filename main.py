"""Des: entry point/code that doesn't fit elsewhere"""

from stats import count_words, count_char, sort_Dict
import sys


def get_book_txt(path):
    """Opens file from path and prints to console"""
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    value = get_book_txt(path)
    count_words(value)
    print("--------- Character Count -------")
    dict = sort_Dict(count_char(value))

    for item in dict:
        print(f"{item["chr"]}: {item["count"]}")

    print("============= END ===============")


main()
