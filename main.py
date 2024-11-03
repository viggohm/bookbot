def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    list_of_letter_count = convert_dict_to_list_of_dict(letter_count)
    report(book_path, word_count, list_of_letter_count)


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

def convert_dict_to_list_of_dict(letter_count):
    list_of_letter_count = []
    for letter in letter_count:
        if letter.isalpha():
            list_of_letter_count.append({"letter": letter, "count": letter_count[letter]})
    
    def sort_on(dict):
        return dict["count"]
    list_of_letter_count.sort(reverse=True, key=sort_on)

    return list_of_letter_count

def report(book_path, word_count, list_of_letter_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for letter_count in list_of_letter_count:
        print(f"The '{letter_count["letter"]}' character was found {letter_count["count"]} times")
    print("--- End report ---")


main()
