#!/usr/bin/env python
# -*- coding:utf-8 -*-
import fileinput
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

mark_result = '报价结果：'
mark_context = '上下文'
mark_log = 'log:'
name_map = {
    'allDailyPv': '全国日均pv',
    'allMonthlyCost': '全国月消耗',
    'basePrice': '底价',
    'qpxBasePrice': '起跑线底价',
    'costFactor': '消耗系数',
    'costPrice': '消耗报价',
    'cpm': '行业CPM',
    'dailyPv': '日均pv',
    'monthlyCost': '月消耗',
    'newWordCost': '新词月消耗',
    'oldWordCost': '旧词月消耗',
    'pcRegionsDailyPv': '所选地区PC日均PV',
    'pcRegionsMonthlyCost': '所选地区PC月消耗',
    'pvFactor': 'PV系数',
    'pvPrice': 'PV报价',
    'qpxPcCpm': '起跑PC行业CPM',
    'qpxWlCpm': '起跑无线行业CPM',
    'quarters': '季度数',
    'regionDailyPv': '所选地区日均PV',
    'regionMonthlyCost': '所选地区月消耗',
    'wlRegionsDailyPv': '所选地区无线日均PV',
    'wlRegionsMonthlyCost': '所选地区无线月消耗',
    'finalPrice': '最终报价',
    'FormulaResult': '公式运算结果',
    'formulaKey': '公式定位key'
}


def parse_part(part):
    print '-----------------------------'
    part = part.replace('{', '\n')
    part = part.replace('}', '')
    for k, v in name_map.items():
        part = part.replace(k, v)
    print part


for line in fileinput.input():
    result_idx = line.find(mark_result)
    if result_idx == -1:
        continue
    context_idx = line.find(mark_context)
    log_idx = line.find(mark_log)
    parse_part(line[result_idx:context_idx])
    parse_part(line[context_idx:log_idx])
    parse_part(line[log_idx:])
