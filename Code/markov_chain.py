from histogram import histogram
from histogram import get_words
import random
from dictogram import Dictogram

def get_corpus(file):
    corpus = get_words(file)
    return corpus

def get_pairs(corpus):
    for index in range(len(corpus)-1):
        yield(corpus[index], corpus[index+1])

def markov_walk(corpus):
    markov_dict = {}
    pairs = get_pairs(corpus)

    for word_1, word_2 in pairs:
        if word_1 in markov_dict.keys():
            markov_dict[word_1].append(word_2)
        else:
            markov_dict[word_1] = [word_2]

    return markov_dict



# def start_word(markov_dict, word):
#     rand_word = random.choice(list(markov_dict.keys()))
#     return rand_word

# def generate_sentence(markov_dict):
#     length = 10
#     first_word = list(markov_dict.keys())[0]
#     second_word = start_word(markov_dict, first_word)
#     sentence = first_word + ' ' + second_word
#     prev_word = second_word

#     for word in range(0, random.randint(1, length)):
#         next_word = start_word(markov_dict, prev_word)
#         prev_word = next_word
#         sentence += next_word + ' '
#     return sentence
if __name__ == '__main__':
    corpus = get_corpus('fish.txt')
    # pairs = get_pairs(corpus)
    # print(pairs)
    chain = markov_walk(corpus)
    print(chain)
    # sentence = generate_sentence(chain)
    # print(sentence)
    