#!/usr/bin/python3

"""Simple commandline tool to read csv files in terminal"""

import argparse
from colorama import Fore, Back, Style
import pandas as pd
import sys

def create_table(csv):
    md = to_markdown(csv)
    return md

def import_csv(args):
    file = args.file
    if args.index:
        csv = pd.read_csv(file)
    else:
        csv = pd.read_csv(file, index=False)
    return csv

def display_file(args):
    """Display csv file as a sorted page or a table"""
    csv = import_csv(args)
    if args.table:
        entry = create_table(csv)
    else:
        entry = csv

    print(entry)

def panic(msg):
    """Error message print"""
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(-1)

def parser_main():
    """Main function initializing ArgumentParser, storing arguments and executing commands."""
    # Top level parser
    parser = argparse.ArgumentParser(
            prog= Style.BRIGHT + 'CSV TERMINAL READER' + Style.RESET_ALL,
            description='''Quickly prints .csv files in terminal''',
            epilog=Style.DIM + '''Code is power!''' + Style.RESET_ALL
        )

    # Parser arguments
    parser.add_argument("-V","--version", action="version", version='%(prog)s 1.0.0')
    parser.add_argument("file", help="csv file name" )
    parser.add_argument("-t","--table", default=False, action="store_true", help="Display csv as a table")
    parser.add_argument("-i","--index", default=True, action="store_false", help="Display csv without an index column")

    parser.set_defaults(func=display_file)
    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError as e:
        msg = f"{e}.\n{Style.BRIGHT}Please run: {Fore.YELLOW}csv --help{Style.RESET_ALL} or read the error message in case your .csv file is corrupted."
        panic(msg)


if __name__ == '__main__':
    parser_main()
  
