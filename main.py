def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = (get_word_count(text))
    letter_count = (get_letter_count(text))
    print_report(get_report(letter_count),word_count,book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = len(text.split())
    return words

def get_letter_count(text):
    #convert to lower case
    lower_case = text.lower()
    #find letter count
    count = {}
    for l in lower_case:
        if l in count:
            count[l] +=1
        else:
            count[l] = 1
    return(count)

def get_report(letter_count):
    count_list = []
    for key,value in letter_count.items():
        if key.isalpha():
            list_dict = {'character': key, 'count': value}
            count_list.append(list_dict)
    count_list.sort(reverse=True, key=sort_on)
    return(count_list)

def sort_on(dict):
        return dict["count"]

def print_report(counts,words,book):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print()
    for c in counts:
        print(f"The '{c['character']}' character was found {c['count']} times")
    print("--- End report ---")

main()
