import random
import sys
from histogram import histogram
from histogram import get_words
from histogram import get_tokens

def print_probability(histogram):
    #gets total count of unique words
    word_count = len(histogram)

    #prints out probability of word being picked
    for key, val in histogram.items():
        print("{} = {}".format(key,val/word_count))

def sample(histogram):
    #gets total count of unique words
    word_count = len(histogram)

    #creating chance variable for random sampling
    chance = 0
    random_num = random.randint(0,1)
    
    #returns random sample word
    for word in histogram:
        chance += histogram[word]/word_count
        if chance >= random_num:
            return word

def test_probability():
    outcomes = {}
    n = 1000

    for i in range(0, n):
       

    
if __name__ == '__main__':
    histo_text = get_words('animals.txt')
    clean_text = get_tokens(histo_text)
    histo = histogram(clean_text)
    sample_word = sample(histo)
    probability = print_probability(histo)
    print(sample_word)
   