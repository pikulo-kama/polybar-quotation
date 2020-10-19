#!/usr/bin/env python3

from helpers import *
import random as rd
import argparse
import os

HOME = os.environ['HOME']
WORKDIR = f'{HOME}/.config/polybar/scripts/quotations/'

configuration = load_json(f'{WORKDIR}conf.json')
c = configuration

QUOTATION_FILE_SEPARATOR = c['separator']

QUOTATIONS_FILE = c['quotation_file_path']
active_quotation = c['active_record_path']

lq, rq = c['left_quote'], c['right_quote']
alq, arq = c['alt_left_quote'], c['alt_right_quote']

LINE_MAX_LENGTH = c['line_max_length']


class Quotation:
    QUOTATION_FILE_PATH = ''
    LINE_MAX_LENGTH = 0

    def __init__(self):
        self.quotes = []
        self.author = ''
        self.line = 0

    def load(self):
        """
        Loads 'active quote' record to object variables.
        """
        data = load_json(active_quotation)

        self.quotes = data['quotes']
        self.author = data['author']
        self.line = data['line']

    def save(self):
        """
        Saves object variables values to active record.
        """
        data = {
            'quotes': self.quotes,
            'author': self.author,
            'line': self.line
        }

        save_json(active_quotation, data)

    @staticmethod
    def random_quote(separator: str):
        """
        Gets random quote from data/quotations.txt
        and saves it to active_record.json file.
        """
        with open(QUOTATIONS_FILE, 'rt') as f:
            content = f.read().splitlines()

        author, quotation = rd.choice(content).split(separator)

        quotation_formatted = q_splitter(quotation, Quotation.LINE_MAX_LENGTH)

        quotation_formatted = [q for q in quotation_formatted if q]

        data = {
            "author": author,
            "quotes": quotation_formatted,
            "line": 0
        }

        save_json(active_quotation, data)

    def get_author(self):
        """
        Returns author of the quote
        """
        self.load()
        return self.author

    def get_full_quote(self):
        """
        Returns full quote
        """
        self.load()
        return ' '.join(self.quotes)

    def next_line(self):
        """
        Increments current line in active quote.
        After last line goes 0.
        """
        self.load()

        last = len(self.quotes) - 1

        if self.line < last:
            self.line += 1
        else:
            self.line = 0

        self.save()

    def get_line(self):
        """
        Returns current line of quote
        """
        self.load()

        return self.quotes[self.line]


if __name__ == '__main__':

    Quotation.QUOTATION_FILE_PATH = QUOTATIONS_FILE
    Quotation.LINE_MAX_LENGTH = LINE_MAX_LENGTH

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a',
        '--author',
        nargs='?',
        const='a',
        metavar='author'
    )

    parser.add_argument(
        '-c',
        '--current-line',
        nargs='?',
        const='a',
        metavar='current_line'
    )

    parser.add_argument(
        '-nl',
        '--next-line',
        nargs='?',
        const='a',
        metavar='next_line'
    )

    parser.add_argument(
        '-f',
        '--full-quote',
        nargs='?',
        const='a',
        metavar='full_quote'
    )

    parser.add_argument(
        '-r',
        '--random-quote',
        nargs='?',
        const='a',
        metavar='random_quote'
    )

    args = parser.parse_args()
    q = Quotation()

    if args.author is not None:
        print(f"{alq} {q.get_author()} {arq}")

    elif args.current_line is not None:

        quote_line = q.get_line()

        first = q.line == 0
        last = q.line == len(q.quotes) - 1
        standalone = len(q.quotes) == 1

        if standalone:
            print(f"{lq}{quote_line}{rq}")
        elif first:
            print(f"{lq}{quote_line}...")
        elif last:
            print(f"..{quote_line}{rq}")
        else:
            print(f"..{quote_line}...")

    elif args.next_line is not None:
        q.next_line()

    elif args.full_quote:
        print(f"{lq}{q.get_full_quote()}{rq}")

    elif args.random_quote:
        Quotation.random_quote(separator=QUOTATION_FILE_SEPARATOR)
