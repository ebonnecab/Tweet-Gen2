from collections import defaultdict

def get_words(file):
  words_list = []  # creates list object
  with open(file) as f:  # accessing word file
    # reads file, strips leading/trailing chars, and retuns a list of strings
    text = f.read().strip().split()
    for word in text:
      words_list.append(word)
    return words_list

def get_anagrams(words_list):
    #default dict creates new entries instead of throwing key error if key doesn't exist
    dict = defaultdict(list)
    for word in words_list:
        key = "".join(sorted(word))
        dict[key].append(word)
    return dict

if __name__ == '__main__':
    words = get_words('/usr/share/dict/words')
    anagrams = get_anagrams(words)
    print(anagrams)