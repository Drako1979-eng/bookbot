# function to count the words in a string and output an integer
def count_words(text_to_count):
    count = 0
    words = text_to_count.split()
    
    for word in words:
        count += 1
    
    return count

# function to count the number of times letters, characters or spaces appear in a string
def count_chars(text_to_parse):
    count = {}
    text_to_parse = text_to_parse.lower()
    letters = list(text_to_parse)
    
    for letter in letters:
        if letter not in count:
            count[letter] = 1
            # print(f"{letter}" + " not in dictionary. Adding.")
        else:
            count[letter] += 1

    return count

def sort_on(items):
    return items['num']

def letter_sort(letter_count):
    dict_list = []
    letter_list = list(letter_count)
    
    for letter in letter_list:
        letter_dict = {'name':letter, 'num': letter_count[letter]}
        dict_list.append(letter_dict)
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list