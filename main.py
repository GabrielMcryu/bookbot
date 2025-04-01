from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        character_count = get_num_words(file_contents)
        return character_count


def main():
    character_count = get_book_text('./books/frankenstein.txt')
    print(character_count)

main()
