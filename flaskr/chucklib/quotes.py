import random

import pathlib
from flaskr.config import BASEDIR

base_dir_path = pathlib.Path(BASEDIR)
quotes_path = base_dir_path / 'chucklib' / 'quotes.txt'


def quote_chuck_norris():
    quotes = []
    for q in open(quotes_path):
        quotes.append(q.replace('\n', ''))
    return random.choice(quotes)
