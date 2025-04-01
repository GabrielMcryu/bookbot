from stats import get_num_words
from stats import sort_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        character_count, total_words = get_num_words(file_contents)
        dict_list = sort_dict(character_count)
        return dict_list, total_words


def main():
    dict_list, total_words = get_book_text("./books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for dict in dict_list:
        if dict["name"].isalpha():
            print(f"{dict["name"]}: {dict["num"]}")


main()
