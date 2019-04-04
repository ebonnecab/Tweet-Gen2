import random
import sys

number = input('Enter number of words: ') #takes user input

def get_words(file):
  words_list = []  # creates list object
  with open(file) as f:  # accessing word file
    text = f.read().strip().split() #reads file, strips leading/trailing chars, and retuns a list of strings
    for word in text:
      words_list.append(word) #appends word  from text to list
    return words_list


def random_sentence(words):
  word_array = random.choices(words, k= int(number)) #picks a random word from list and stores in an array
  sentence = ' '.join(word_array) + '.' #joins words into a sentence
  sentence = sentence.capitalize() #capitalizes beginning of sentence
  return sentence

    
if __name__ == '__main__':
  source = get_words('/usr/share/dict/words')
  words_list = source
  test = random_sentence(words_list)
  print(test)