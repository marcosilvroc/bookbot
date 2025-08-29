def get_num_words(text):
    number_words = len(text.split())
    return number_words

def get_num_char(text):
    char_dict = {}
    for char in text.lower():
        if(char in char_dict):
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_number_char_dict(dict, pos):
    if(dict[pos]["num"]):
        return dict[pos]["num"]
    else:
        return None

def get_num(item):
    return item["num"]

def sort_dict(dict):
    unsorted_dict = list()
    for k in dict:
        unsorted_dict.append(
            {
            "char": k,
            "num": dict[k]
        })
    #print("test: ", get_num(unsorted_dict[0]))
    unsorted_dict.sort( key=get_num, reverse = True)
    return unsorted_dict

def print_bookbot(filepath, words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for c in sorted_list:
        if(c["char"].isalpha()):
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")
    return
