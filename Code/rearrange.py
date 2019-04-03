#function that takes a command line argument and randomly rearranges a set of words
import random 
import sys

word_array = sys.argv[1:]

def word_shuffle():
    for index in range(len(word_array)-1,0,-1): #accesses index of argument
        random_index = random.randint(0, index) #picks a random number between zero and len of array
        word_array[index] = word_array[index].lower() #converts string to lowercase
        word_array[index], word_array[random_index] = word_array[random_index], word_array[index] #swaps original index with rand index

    #joining word array into a sentence
    sentence = ' '.join(word_array) + '.'
    sentence = sentence.capitalize()
    return sentence

if __name__ == '__main__':
    print(word_shuffle())