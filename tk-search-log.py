#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
错误日志提取

Usage:
  search-log.py [--line-pattern=<line-pattern>] [--search-pattern=<search-pattern>] <file>...
  search-log.py -h | --help

Options:
  -h --help     Show this screen.
  -l --line-pattern 行开始标志（正则表达式）。
  -s --search-pattern 搜索字符串，（正则表达式）。
"""

import sys
import fileinput
import re
from docopt import docopt

reload(sys)
sys.setdefaultencoding('utf-8')

arguments = docopt(__doc__, version='Naval Fate 2.0')
#print(arguments)

block_hit = True
search_hit = False

line_pattern_str = arguments['--line-pattern'] if arguments['--line-pattern'] is not None else '^\s*\[?\d{4}-\d{2}-\d{2}\s'
search_pattern_str = arguments['--search-pattern'] if arguments['--search-pattern'] is not None else '\[(ERROR)\]|(Exception)'
re_flag = re.I | re.M | re.U
block_pattern = re.compile(line_pattern_str, re_flag)
search_pattern = re.compile(search_pattern_str, re_flag)

block_lines = []

def hit_search():
    if not block_lines:
        return False
    for line in block_lines:
        if search_pattern.search(line) is not None:
            return True
    return False


def print_block_lines():
    if not block_lines:
        return
    for l in block_lines:
        print l,

for line in fileinput.input(arguments['<file>']):
    hit_new_line = block_pattern.search(line) is not None
    if hit_new_line:
        if hit_search():
            print_block_lines()
        block_lines = []
    block_lines.append(line)

if hit_search():
    print_block_lines()
