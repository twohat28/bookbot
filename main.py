def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    char_list = char_dict_to_list(chars_dict)

    print(f"- - - Begin report of {book_path} - - -")
    print(f"{num_words} words found in the document")
    print()

    for i in char_list:
        if not i["character"].isalpha():
            continue
        print(f"The {i['character']} character was found {i['count']} times")
    
    print("- - - End report - - -")
    
def char_dict_to_list(x):
    y = []
    for i in x:
        y.append({"character":i, "count":x[i]})
    y.sort(reverse = True, key = sort_by_count)
    return y

def sort_by_count(x):
    return x["count"]  

def get_chars_dict(t):
    x = t.lower()
    y = {}
    for a in x:
        if a in y:
            y[a] += 1
        else:
            y[a] = 1
    return y

def get_num_words(txt):
    words = txt.split()
    return len(words)

def get_book_text(p):
    with open(p) as f:
        return f.read()
    
main()