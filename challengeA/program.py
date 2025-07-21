#! /usr/bin/env python3
# print("Hello world")

import sys

def find_sunrise(b):
    cur_max = float("-inf")
    res = 0
    for i in range(len(b)-1,-1,-1):
        if cur_max < b[i]:
            res += 1
            cur_max = b[i]
    print(res)
        






for line in sys.stdin:
    line = list(map(int,line.strip().split()))
    # print(line)
    find_sunrise(line)

