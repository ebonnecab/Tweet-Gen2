#!/usr/bin/python3
import random
import sys
from histogram import histogram
from histogram import get_words
from histogram import get_tokens
from histogram import listogram

def print_probability(histogram):
    #gets total count of unique words
    word_count = sum(histogram.values())

    #prints out probability of word being picked
    for key, val in histogram.items():
        print("{} = {}".format(key,val/word_count))

def sample(histogram):
    #gets total count of unique words
    word_count = sum(histogram.values())

    #creating chance variable for random sampling
    chance = 0
    random_num = random.random()
    
    #returns random sample word
    for word in histogram:
        chance += histogram[word]/word_count
        if chance >= random_num:
            return word

def test_probability(histogram):
    #created dict to store results
    outcomes = []
    #the number of times I want to run the test
    n = 1000

    #appending sample word to list n times
    for i in range(0, n):
        outcomes.append(sample(histogram))
    return outcomes

def results_histogram(outcomes):
    #storing outcomes and freq in this empty dict
    results = {}

    for word in outcomes:
        if word in results:
            results[word] +=1
        else:
            results[word] = 1
    
    return results

if __name__ == '__main__':
    histo_text = get_words('animals.txt')
    clean_text = get_tokens(histo_text)
    histo = histogram(clean_text)
    sample_word = sample(histo)
    probability = print_probability(histo)
    # print(sample_word)
    outcomes = test_probability(histo)
    results = results_histogram(outcomes)
    print(results)
    
   