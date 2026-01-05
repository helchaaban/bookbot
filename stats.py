



def get_words(booktext):
    word_count = len(booktext.split())
    return print(f"Found {word_count} total words")

def get_letters(booktext):
    letter_count = {}
    letter_list = list(booktext.lower())
    for letter in letter_list:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] = letter_count[letter] + 1

    
    return print(letter_count)

def sort_dict(dict):
    dict.sort()