def get_num_words(text):
    return len(text.split())

def get_letter_count(text):
    lower_no_space_text = list(text.lower().replace(" ", ""))
    frequency = {}

    for letter in lower_no_space_text:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    return frequency

def sort_chars(dictionary):
    list = []

    for item in dictionary:
        print(item)
        list.append({"char": item , "count": dictionary[item]})


    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dictionary):
    return dictionary["count"]
