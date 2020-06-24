#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

regionsMap = {
    1: "全部",
    2: "北京",
    3: "天津",
    4: "河北",
    5: "山西",
    6: "内蒙古",
    7: "吉林",
    8: "辽宁",
    9: "黑龙江",
    10: "上海",
    11: "福建",
    12: "安徽",
    13: "江苏",
    14: "江西",
    15: "山东",
    16: "浙江",
    17: "河南",
    18: "湖北",
    19: "湖南",
    20: "广东",
    21: "广西",
    22: "海南",
    23: "贵州",
    24: "四川",
    25: "西藏",
    26: "云南",
    27: "重庆",
    28: "甘肃",
    29: "宁夏",
    30: "青海",
    31: "陕西",
    32: "新疆",
    33: "海外港澳台"
}

if len(sys.argv) != 2:
    usage = '''
使用：python %s <地域字段Long值>
    ''' % sys.argv[0]
    print usage
    sys.exit(-1)

region_id = int(sys.argv[1])
for k, v in regionsMap.items():
    mask = 1 << (33 - k)
    if mask & region_id == mask:
        print v
