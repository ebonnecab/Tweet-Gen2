from histogram import histogram
from histogram import get_words
import random
from dictogram import Dictogram

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
            markov_dict[word_1].append(word_2)
        else:
            markov_dict[word_1] = [word_2]

    return markov_dict

def start_word(markov_dict):
    rand_word = random.choice(list(markov_dict.keys()))
    return rand_word

def generate_sentence(markov_dict):
    length = 10
    first_word = list(markov_dict.keys())[0]
    second_word = start_word(markov_dict)
    sentence = first_word + ' ' + second_word

    for word in range(0, random.randint(1, length)):
        next_word = start_word(markov_dict)
        sentence += ' ' + next_word + ' '
    return sentence
if __name__ == '__main__':
    corpus = get_corpus('siddhartha.txt')
    chain = markov_walk(corpus)
    sentence = generate_sentence(chain)
    print(sentence)
    