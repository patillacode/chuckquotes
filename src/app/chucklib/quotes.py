"""
Created on Jan 18, 2016

@author: Patilla Code <patillacode@gmail.com>
@usage: python quotes.py

Prints a random Chuck Norris quote.
"""

import random
import os


def quote_chuck_norris():
    quotes = []
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        ('quotes.txt'))
    for q in open(file_path):
        quotes.append(q.replace('\n', ''))
    return random.choice(quotes)


if __name__ == '__main__':
    print '\n', quote_chuck_norris()
