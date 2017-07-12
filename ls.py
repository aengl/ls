#!/usr/bin/env python3

import os
import re
import sys
import argparse

try:
    from colored import fg, attr
except ImportError:
    def fg(*args):
        return ''

    def attr(*args):
        return ''

# Color chart: https://pypi.python.org/pypi/colored/1.3.3
COLORS = [11, 118, 117, 105, 7]
RE_PRIORITY = r'\(([A-Z])\)'
RE_CONTEXT_OR_PROJECT = r'([@+][^\s]+)'


def get_priority(line):
    match = re.search(RE_PRIORITY, line)
    return match and match.group(1) or None


def get_priority_as_number(line, maximum=sys.maxsize):
    priority = get_priority(line)
    if priority == None:
        return maximum
    return min(maximum, ord(priority) - ord('A'))


def print_item(linenum, line):
    color_index = get_priority_as_number(line, maximum=len(COLORS) - 1)
    color = fg(COLORS[color_index])
    line = re.sub(RE_PRIORITY + ' ', '', line)
    line = re.sub(RE_CONTEXT_OR_PROJECT, attr(2) +
                  color + r'\1' + attr(0) + color, line)
    line = attr(0) + color + line
    print('{:}{:02d} {:}'.format(attr(2) + color, linenum, line))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")
    args = parser.parse_args()
    with open(os.path.join(args.dir, 'todo.txt'), 'r') as todofile:
        linenums_and_lines = [(index + 1, line)
                              for index, line in enumerate(todofile.readlines())]
    for linenum, line in sorted(linenums_and_lines, key=lambda x: get_priority_as_number(x[1])):
        print_item(linenum, line.strip())


if __name__ == '__main__':
    main()
