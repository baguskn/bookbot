def get_book_txt(path):
    with open(path) as f:
        return f.read()
    
def main():
    path = "books/frankenstein.txt"
    print(get_book_txt(path))

main()