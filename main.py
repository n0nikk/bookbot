def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_dict = get_chars_dict(text)
    alphabet_list = get_alphabet_list(chars_dict)
    clean_list = get_clean_list(alphabet_list)
    print_report(text, book_path, clean_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_alphabet_list(dict):
    chars_list = list(dict.items())
    sorted = chars_list.sort(key = lambda x: x[1], reverse= True)
    return chars_list

def get_clean_list(lists):
    clean_list = []
    for list in lists:
        first_item = list[0]
        if first_item.isalpha():
            clean_list.append(list)
    return clean_list



def print_report(text, book_path, clean_list):
    print(f"-- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    for list in clean_list:   
        print(f"The {list[0]} character was found {list[1]} times")
    print("--- End report ---")

    
main()