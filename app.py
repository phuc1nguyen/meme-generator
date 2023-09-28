"""Implementation of the Flask server for Meme Generator.

See `README.md` for more details on how to use this generator.
"""

import random
import os
import requests
from datetime import datetime
from flask import Flask, render_template, abort, request

from modules.Ingestors import Ingestor
from modules.MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = []
    for dirpath, dirnames, filenames in os.walk(images_path):
        imgs = [os.path.join(dirpath, name) for name in filenames]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    data = request.form
    image_url = data['image_url']
    body = data['body']
    author = data['author']

    response = requests.get(image_url, stream=True).content
    image_ext = image_url.split('.')[-1]
    tmp = f"./tmp/{round(datetime.now().timestamp())}.{image_ext}"
    with open(tmp, 'wb') as img:
        img.write(response)

    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
