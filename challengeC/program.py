#! /usr/bin/env python3
# print("Hello world")

import sys

def solve_val(num_op,ops,t):
    if num_op == 8:
        f_val = f"(((9 {ops[0]} 8) {ops[1]} 7) {ops[2]} 6) {ops[3]} (5 {ops[4]} (4 {ops[5]} (3 {ops[6]} (2 {ops[7]} 1))))"
        res = eval(f_val)
        if res == t:
            print(f"{f_val} = {res}")
            return True
        return False

    
    for o in ["+", "-", "*"]:
        num_op += 1
        ops.append(o)

        if solve_val(num_op,ops,t):
            return True
        num_op -= 1
        ops.pop()
    return False


for line in sys.stdin:
    t = int(line.strip())
    ans = solve_val(0,[],t)

