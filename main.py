def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print(word_count)
    print(letter_count) 

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    letter_count = {}
    book = book.lower()
    for letter in book:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

main()
