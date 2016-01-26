"""
Created on Jan 18, 2016

@author: Patilla Code <patillacode@gmail.com>
@usage: python quotes.py

Prints a random Chuck Norris quote.
"""

import random


def quote_chuck_norris():
    quotes = []
    for q in open('chucklib/quotes.txt'):
        quotes.append(q.replace('\n', ''))
    return random.choice(quotes)


if __name__ == '__main__':
    print '\n', quote_chuck_norris()
