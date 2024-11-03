with open("books/frankenstein.txt") as f:
    file_content = f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = count_words(text)
    print(word_count)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

main()
