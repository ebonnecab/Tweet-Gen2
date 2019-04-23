from histogram import histogram
from histogram import get_words
import random
from dictogram import Dictogram

def get_corpus(file):
    corpus = get_words(file)
    return corpus

def markov_walk(corpus):
    markov_dict = {}
    
    for word in corpus:
        if word not in markov_dict:
            markov_dict[word] = {}
    
    index = 0
    if index + 1 < len(corpus):
        next_word = corpus[index+1]
        if next_word in markov_dict[word].keys():
            markov_dict[word][next_word] += 1
        else:
            markov_dict[word][next_word] = 1
        index +=1
    print(index)
    return markov_dict

def start_word(markov_dict, word):
    rand_word = random.choice(list(markov_dict.keys()))
    return rand_word

def sentence_generator(markov_dict):
    length = 10
    first_word = list(markov_dict.keys())[0]
    second_word = start_word(markov_dict, first_word)
    sentence = first_word + ' ' + second_word
    prev_word = second_word

    for word in range(0, random.randint(1, length)):
        next_word = start_word(markov_dict, prev_word)
        prev_word = next_word
        sentence += next_word + ' '
    return sentence
if __name__ == '__main__':
    corpus = get_corpus('siddhartha.txt')
    chain = markov_walk(corpus)
    sentence = sentence_generator(chain)
    print(sentence)
    