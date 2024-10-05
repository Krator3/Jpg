#!/usr/bin/env python3

# Библиотеки
import argparse
import sys
# Файлы программы
from detect import *
import functions.hide as hide
import functions.search as search

parser = argparse.ArgumentParser(prog=prog, description=description)

parser.add_argument("hide", nargs="*", help=help_hide)
parser.add_argument("search", nargs="*", help=help_search)
parser.add_argument("-c", "--clear", action="store_false", help=help_clear)
parser.add_argument("-v","--version", action="store_true", help=help_version)

args = parser.parse_args()

try:
    if args.version:
        print("jpg v1.0.0")

    elif len(sys.argv) < 2:
        print(no_data)

    elif "hide" in sys.argv:
        if len(sys.argv) >= 4:
            print(sys.argv[::])
            hide.hide_func(jpg_path=sys.argv[2], hide_path=sys.argv[3])
        else:
            print(error_path)

    elif "search" in sys.argv:
        if len(sys.argv) >= 3:
            search.search_func(jpg_path=sys.argv[2])
        else:
            print(error_path)
    else:
        print(arguments_not_supported)
except:
    print(error_base)
finally:
    print(done)

