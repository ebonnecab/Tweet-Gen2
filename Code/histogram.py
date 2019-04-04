import random

def histo_file (file):
    with open(file) as f:  # access file
        # reads file, strips leading/trailing chars, and retuns a list of strings
        text = f.read().strip().split()
        return text

def histogram(text):
    dict = {}  # creates empty dict
    for word in text: #adding word and word frequency as key,val pairs
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    
    return dict

def unique_words(histogram):
    
    return len(histogram) #returns number of unique words stored in histogram

def frequency(word, histogram):
    if word in histogram: #checks if word is in histogram
        return histogram[word] #returns key value pairs
    else:
        return "That word is not in the histogram"  #returns error msg


'''
List Implementation of Histogram
'''
def listogram():
    sample_sentence = "one fish two fish red fish blue fish"
    word_array = sample_sentence.split(" ") #splits string into list of individual strings
    words_list = [] #creates empty list object
    for word in word_array: #accessing word in array
        for index in words_list: #accessing index of words list
            if index[0] == word: #counting word freq for each word and creating 2d array
                index[1] += 1
        words_list.append([word, 1]) #appending word and word freq to list
    return words_list

if __name__ == '__main__':
    # histo_text = histo_file('siddhartha.txt')
    # histo = histogram(histo_text)
    # print(histo)
    listo = listogram()
    print(listo)
    # print(unique_words(histo))

    # print(frequency('he', histo))
