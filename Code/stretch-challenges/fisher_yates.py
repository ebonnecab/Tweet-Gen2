#takes an array as input 
#outputs a randomized version of the input

import random

def shuffle_deck(array):
    for index in range(len(array) -1, 0, -1): #this function accesses the index of array
        rand_num = random.randint(0,index+1) #pick a random number between zero and index
        array[index], array[rand_num] = array[rand_num], array[index] #swap index with element at random number
    return array

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':
    print(shuffle_deck(array))