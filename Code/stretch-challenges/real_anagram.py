from collections import defaultdict

def get_words():
  words_list = []  # creates list object
  with open('/usr/share/dict/words') as file:  # accessing word file
    # reads file, strips leading/trailing chars, and retuns a list of strings
    text = file.read().strip().split()
    for word in text:
      words_list.append(word)
    return words_list

def get_anagrams(words_list):
    dict = defaultdict(list)
    for word in words_list:
        key = "".join(sorted(word))
        dict[key].append(word)
    return dict

def print_anagrams():
    return