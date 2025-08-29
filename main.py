from stats import get_num_words, get_num_char, sort_dict, print_bookbot

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

    return None

def main():
    text = get_book_text("books/frankenstein.txt")
    """
    Sanity check
    print(len(text))           # total characters
    print(text[:100])          # start
    print(text[-100:])         # end
    """
    words = get_num_words(text)
    dict = sort_dict(get_num_char(text))
    print_bookbot("books/frankenstein.txt", words, dict)
    return

main()
