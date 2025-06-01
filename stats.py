def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    dict = {}
    for char in text:
        char = char.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def get_sorted_alpha_dict(chars_dict):
    alpha_dict = {}
    for char in chars_dict:
        if char.isalpha():
            alpha_dict[char] = chars_dict[char]
    sorted_dict = dict(sorted(alpha_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

            
