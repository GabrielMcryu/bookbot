from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        return num_words


def main():
    num_words = get_book_text('./books/frankenstein.txt')
    print(f'{num_words} words found in the document')

main()
