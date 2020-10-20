#!/usr/bin/env python3

from helpers import *
import random as rd
import subprocess
import argparse
import os

HOME = os.environ['HOME']
WORKDIR = f'{HOME}/.config/polybar/scripts/polybar-quotation'

configuration = load_json(f'{WORKDIR}/conf.json')
c = configuration

QUOTATION_FILE_SEPARATOR = c['separator']

QUOTATIONS_FILE = f"{WORKDIR}/data/{c['quotation_file']}"
active_quotation = f"{WORKDIR}/data/{c['active_record']}"
bar_name = c['bar_name']

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

    @staticmethod
    def set_status(status):
        """
        Sets scrolling status
        """
        if status not in ('PLAY', 'PAUSE'):
            raise ValueError("Invalid Status. Use PLAY or PAUSE")

        data = load_json(active_quotation)
        data['status'] = status

        save_json(active_quotation, data)

    @staticmethod
    def get_status():
        """
        Returns status of quote.
        If status not set - sets PAUSE as default
        """
        try:
            status = load_json(active_quotation)['status']
        except KeyError:
            Quotation.set_status('PAUSE')
        return status

    @staticmethod
    def swap_status():
        """
        Swaps status of quote
        """
        status = 'PAUSE' if Quotation.get_status() == 'PLAY' else 'PLAY'

        hook_id = 2 if status == 'PAUSE' else 1
        pid_of_bar = str(subprocess.run(['pgrep', '-f', f'polybar {bar_name}'],
                                        stdout=subprocess.PIPE).stdout)[2:-3]

        os.system(f'polybar-msg -p {pid_of_bar} hook quote-control {hook_id}')
        Quotation.set_status(status)

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

    parser.add_argument(
        '--swap',
        nargs='?',
        const='a',
        metavar='swap'
    )

    parser.add_argument(
        '--status',
        nargs='?',
        default='get_status',
        const='get_status',
        metavar='status'
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
        print(f"{lq}{q.get_full_quote()}{rq}  -  {alq}{q.get_author()}{arq}")

    elif args.random_quote:
        Quotation.random_quote(separator=QUOTATION_FILE_SEPARATOR)

    elif args.swap is not None:
        Quotation.swap_status()
        print(Quotation.get_status())

    elif args.status == 'get_status':
        print(Quotation.get_status())

    elif args.status is not None:
        Quotation.set_status(args.status)
