from stats import get_words, get_letters, sort_dict


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    get_words(text)
    sort_dict(get_letters(text))
    

def get_book_text(path):
    with open(path) as f:
        return f.read()














main()