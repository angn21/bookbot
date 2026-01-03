def get_num_words(book):
    b_split = book.split()
    return len(b_split)

def get_num_char(book):
    book_lower = book.lower()
    count = {}
    for char in book_lower:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1
    return count

def sort_on_num(item):
    return item["num"]

def sorted_dict(book):
    count = get_num_char(book)
    char_count_list = []
    for char, num in count.items():
        char_count_list.append({"char": char, "num": num})
    char_count_list.sort(key=sort_on_num, reverse=True)
    return char_count_list
