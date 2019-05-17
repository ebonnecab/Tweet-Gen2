from nltk import word_tokenize
import string

def read_file(file):
    with open(file) as f:  # access file
        text = f.read()
    
    return text

def get_tokens(text):
    #split text into word tokens
    tokens = word_tokenize(text)
    #converts tokens to lowercase
    tokens = [word.lower() for word in tokens]
    #removes punctuation from each word
    table = str.maketrans('', '', string.punctuation) 
    stripped = [w.translate(table) for w in tokens]
    #remove non-alphabetic tokens
    words = [word for word in stripped if word.isalpha()]

    return words

#opens a new file and writes newly cleaned corpus to that file

def write_data(file, corpus):
    with open(file, 'w+') as f:
        for word in corpus:
            f.write(word + " ")


if __name__ == '__main__':
    text = read_file('alice.txt')
    tokens = get_tokens(text)
    corpus = write_data('corpus.txt', tokens)