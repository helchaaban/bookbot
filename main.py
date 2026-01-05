from stats import get_words, get_letters, chars_dict_to_sorted_list
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print("=============BOOKBOT=============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------------WORD COUNT---------")
    get_words(text)
    print("------------------Character Count-----------")
    sorted_dict_list = chars_dict_to_sorted_list(get_letters(text))

    for item in sorted_dict_list:
        ch = item["char"]
        num = item["num"]
        print(f"{ch}: {num}")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()














main()