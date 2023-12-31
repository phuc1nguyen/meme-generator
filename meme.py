"""Implementation of the CLI tool for Meme Generator.

See `README.md` for more details on how to use this generator.
"""

import os
import argparse
import random

from modules.Ingestors import Ingestor
from modules.QuoteEngine import Quote
from modules.MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = Quote(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate meme using command-line.')
    parser.add_argument('-p', '--path', type=str, nargs='+',
                        help='path to an image file', default=None)
    parser.add_argument('-b', '--body', type=str,
                        help='quote body to add to the image', default=None)
    parser.add_argument('-a', '--author', type=str,
                        help='quote author to add to the image', default=None)
    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
