from flask import Flask
from histogram import histogram
from histogram import histogram
from histogram import get_words
from histogram import get_tokens
from histogram import listogram
from sample import sample

HTML="""<html><head><title>My App</title></head>
        <body><h2>{}</h2></body"""
app = Flask(__name__)

@app.route('/')
def hello_world():
    histo_text = get_words('animals.txt')
    clean_text = get_tokens(histo_text)
    histo = histogram(clean_text)
    random_word = sample(histo)
    return HTML.format(random_word)