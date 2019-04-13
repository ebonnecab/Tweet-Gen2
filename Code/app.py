from flask import Flask
from histogram import histogram
from histogram import histogram
from histogram import get_words
from histogram import listogram
from sample import sample
from rearrange import sentence_maker

HTML="""<html><head><title>My App</title></head>
        <body><h2>{}</h2></body"""
app = Flask(__name__)

@app.route('/words/<int:num>')
def hello_world(num):
    histo_text = get_words('siddhartha.txt')
    histo = histogram(histo_text)
    random_word = sample(histo)
    random_words = []
    for i in range(num):
        random_words.append(sample(histo))
    random_sentence = sentence_maker(random_words)
    return HTML.format(random_sentence)

 if __name__ == '__main__':
     app.debug = True
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)
