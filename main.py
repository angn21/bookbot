from stats import get_num_words, sorted_dict
import sys

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():

    if (len(sys.argv) - 1 < 1):
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = str(sys.argv[1])
        book = get_book_text(book_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(book)} total words")
        print("--------- Character Count -------")

        sorted_chars = sorted_dict(book)

        for item in sorted_chars:
            ch = item["char"]
            if not ch.isalpha():
                continue
            print(f"{ch}: {item['num']}")

        print("============ END ============")

main()