



def get_words(booktext):
    word_count = len(booktext.split())
    print(f"Found {word_count} total words")
    return word_count  # no print here


def get_letters(booktext):
    letter_count = {}
    letter_list = list(booktext.lower())
    for letter in letter_list:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] = letter_count[letter] + 1
    return letter_count  # return the dict, don't print

    
    return letter_count

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
        else:
            continue
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list