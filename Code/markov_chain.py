from histogram import histogram
from histogram import get_words
from sample import sample
from dictogram import Dictogram
from listogram import Listogram
import random

'''
uses imported function to get individual words from corpus
'''
def get_corpus(file):
    corpus = get_words(file)
    return corpus

'''
this function accesses each word in the corpus
yields that word + the word that follows
'''
def get_pairs(corpus):
    for index in range(len(corpus)-1):
        yield(corpus[index], corpus[index+1])

'''
this function stores each individual word as keys
and appends their pairs as values for that key
'''
def markov_walk(corpus):
    markov_dict = {}
    pairs = get_pairs(corpus)
    
    for word_1, word_2 in pairs:
        if word_1 in markov_dict.keys():
            markov_dict[word_1].add_count(word_2)
        else:
            markov_dict[word_1] = Dictogram([word_2])

    return markov_dict

#trying to refactor account for word freq

    #  for word_1, word_2 in pairs:
    #     if word_1 in markov_dict.keys():

    #         markov_dict[word_1].append((word_2, count))
    #     else:
    #         markov_dict[word_1] = [(word_2, count)]

    # return markov_dict

''' 
Picks a random start word for markov walk from list of dict keys
'''
def start_word(markov_dict):
    rand_word = random.choice(list(markov_dict.keys()))
    return rand_word

'''
doing a markov walk to create a sentence from dictionary
generated above. once key is accessed, a random pairing is picked
from the values associated and the markov walk restarts
for random length of sentence
'''
def generate_sentence(markov_dict):
    length = 10
    first_word = start_word(markov_dict)
    sentence = first_word.capitalize()

    for word in range(0, random.randint(1, length)):
        second_word = random.choice(markov_dict[first_word])
        first_word = second_word
        sentence += ' ' + second_word
    
    return sentence


if __name__ == '__main__':
    corpus = get_corpus('fish.txt')
    chain = markov_walk(corpus)
    print(chain)
    # sentence = generate_sentence(chain)
    # print(sentence)
    
