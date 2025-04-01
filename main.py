def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    contents = get_book_text('./books/frankenstein.txt')
    print(contents)

main()
