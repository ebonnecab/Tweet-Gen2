import random
import sys

number = input('Enter number of words: ') #takes user input

def get_words(file):
  words_list = []  # creates list object
  with open(file) as f:  # accessing word file
    #reads file, strips leading/trailing chars, and retuns a list of strings
    text = f.read().strip().split()
    return text


def random_sentence(words):
  #picks a random word from list and stores in an array
  word_array = random.choices(words, k= int(number))
  sentence = ' '.join(word_array) + '.' #joins words into a sentence
  sentence = sentence.capitalize() #capitalizes beginning of sentence
  return sentence

    
if __name__ == '__main__':
  source = get_words('/usr/share/dict/words')
  test = random_sentence(source)
  print(test)
