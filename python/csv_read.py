#!/usr/bin/python3

"""Simple commandline tool to read csv files in terminal"""

import argparse
from colorama import Fore, Back, Style
import pandas as pd
import sys

def create_markdown(csv, args):
    if args.index == True:
        md = csv.to_markdown()
    else:
        md = csv.to_markdown(index=False)
    return md

def create_table(csv, args):
    if args.index == True:
        table = csv.to_markdown(tablefmt="grid")
    else:
        table = csv.to_markdown(tablefmt="grid", index=False)
    return table

def import_csv(args):
    file = args.file
    if args.index == True:
        csv = pd.read_csv(file)
    else:
        csv = pd.read_csv(file, index_col=False)
        csv.reset_index(drop=True, inplace=True)
    return csv

def display_file(args):
    """Display csv file as a sorted page or a table"""
    csv = import_csv(args)
    if args.table:
        data = create_table(csv, args)
    elif args.markdown:
        data = create_markdown(csv, args)
    else:
        data = csv

    print(data)

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
    parser.add_argument("-m","--markdown", default=False, action="store_true", help="Display csv in markdown")
    parser.add_argument("-t","--table", default=False, action="store_true", help="Display csv as a table")
    parser.add_argument("-i","--index", default=True, action="store_false", help="Display csv without an index column (works only with -m and -t options")

    parser.set_defaults(func=display_file)
    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError as e:
        msg = f"{e}.\n{Style.BRIGHT}Please run: {Fore.YELLOW}csv --help{Style.RESET_ALL} or read the error message in case your .csv file is corrupted."
        panic(msg)


if __name__ == '__main__':
    parser_main()
