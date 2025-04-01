from stats import get_num_words
from stats import sort_dict
import sys

def get_book_text(path):
    with open(path, "r") as f:
        file_contents = f.read()
        character_count, total_words = get_num_words(file_contents)
        dict_list = sort_dict(character_count)
        return dict_list, total_words


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    dict_list, total_words = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for dict in dict_list:
        if dict["name"].isalpha():
            print(f"{dict["name"]}: {dict["num"]}")


main()
