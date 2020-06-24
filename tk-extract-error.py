#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
错误日志提取

Usage:
  extract-error.py [--line-pattern=<line-pattern>] [--error-pattern=<error-pattern>] <file>...
  extract-error.py -h | --help

Options:
  -h --help     Show this screen.
  -l --line-pattern 行开始标志（正则表达式）。
  -e --error-pattern 异常标志（正则表达式）。
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
error_hit = False

line_pattern_str = arguments['--line-pattern'] if arguments['--line-pattern'] is not None else '^\s*\[?\d{4}-\d{2}-\d{2}\s'
error_pattern_str = arguments['--error-pattern'] if arguments['--error-pattern'] is not None else '\[(ERROR|WARN)\]|(Exception)'
re_flag = re.I | re.M | re.U
block_pattern = re.compile(line_pattern_str, re_flag)
error_pattern = re.compile(error_pattern_str, re_flag)

for line in fileinput.input(arguments['<file>']):
    block_hit = block_pattern.search(line) is not None
    if block_hit:
        if error_pattern.search(line) is not None:
            error_hit = True
        else:
            error_hit = False
    if error_hit:
        print line,
