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
COLORS = {
    'A': fg(11),
    'B': fg(118),
    'C': fg(117),
    'D': fg(105),
}
RE_PRIORITY = r'\(([A-Z])\)'
RE_CONTEXT_OR_PROJECT = r'([@+][^\s]+)'


def get_priority(line):
    match = re.search(RE_PRIORITY, line)
    return match and match.group(1) or None


def get_priority_as_number(line):
    priority = get_priority(line)
    return priority and ord(priority) or sys.maxsize


def print_item(linenum, line):
    color = COLORS.get(get_priority(line), fg(7))
    line = re.sub(RE_PRIORITY + ' ', '', line)
    line = re.sub(RE_CONTEXT_OR_PROJECT, attr(2) +
                  color + r'\1' + attr(0) + color, line)
    line = attr(0) + color + line
    print('{:}{:02d} {:}'.format(attr(2) + color, linenum, line))


def read_file(path):
    with open(path, 'r') as todofile:
        linenum_and_line = []
        linenum = 1
        for line in todofile.readlines():
            linenum_and_line.append((linenum, line))
            linenum += 1
        return linenum_and_line


def main(root):
    if not os.path.isdir(root):
        print("Error: %s is not a directory" % args.dir)
        sys.exit(1)
    linenum_and_line = read_file(os.path.join(root, 'todo.txt'))
    for linenum, line in sorted(linenum_and_line, key=lambda x: get_priority_as_number(x[1])):
        print_item(linenum, line.strip())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")
    parser.add_argument(
        "share", nargs="?", help="absolute or relative path to the share")
    args = parser.parse_args()
    main(args.share and os.path.abspath(
        os.path.join(args.dir, args.share)) or args.dir)
