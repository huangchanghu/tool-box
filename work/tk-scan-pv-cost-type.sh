#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import fileinput
reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) == 1:
  usage =  '''
  Info:  从日志中获取报价中用到的PvCostType 
  Usage: python %s <log file list> 
  ''' % sys.argv[0]
  print usage
  sys.exit(-1)

for line in fileinput.input():
  idx = line.find('pvCostType=')
  if idx == -1: 
    continue
  sub = line[idx + 11:]
  print sub[0:sub.find(',')]
  

