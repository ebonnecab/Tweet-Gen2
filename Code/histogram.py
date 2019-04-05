import random

def get_words(file):
    words_list = []
    with open(file) as f:  # access file
        #access each line of file
        for line in f:
            #splits line into list of words
            text = line.split()
            for word in text: #accessing each word
                word.strip() #strips trailing/leading chars
                words_list.append(word) #appending words to list
    return words_list


''' 
Dictionary Implementation of Histogram
'''
        
 #adding word and word frequency as key,val pairs
def histogram(text):
    dict = {}  # creates empty dict
    for word in text:
        #check if word is in dict
        if word in dict:
        #increase count by 1
            dict[word] += 1
        else:
        #set count to 1
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


def unique_words(listogram):
    # returns number of unique words stored in histogram
    return len(listogram)


# def frequency(word, listogram):
#     if word in listogram:  # checks if word is in histogram
#         return listogram[index]  # returns key value pairs
#     else:
#         return "That word is not in the listogram"  # returns error msg
    
'''
Tuples Implementation of Histogram
'''
def tuplegram():
    sample_sentence = "one fish two fish red fish blue fish"
    word_array = sample_sentence.split() #splits string into list of individual strings
    words_list = [] #creates empty list object
    #accesses word in array
    for word in word_array: 
        found = False
        for index in words_list:
            if index[0] == word:
                freq = index[1] + 1
                words_list.remove(index)
                words_list.append((word, freq))
                found = True
        if not found:
            words_list.append((word, 1))
    
    return words_list
if __name__ == '__main__':
    histo_text = get_words('siddhartha.txt')
    # histo = histogram(histo_text)
    # print(histo)
    # print(unique_words(histo))
    # print(frequency('he', histo))

    listo = listogram()
    print(listo)
    print(unique_words(listo))
    # print(frequency('fish', listo))

    # tuplegram = tuplegram()
    # print(tuplegram)
