#! /usr/bin/env python3
# print("Hello world")

import sys

# def solve_fb(score_list,score,t,res):
#     if score == t:
#         score_list=sorted(score_list)
#         if score_list not in res:
#             res.append(score_list[:])
#         return True
#     if score > t:
#         return False
#     for i in [2,3,7]:
#         score_list.append(i)
#         score += i
#         solve_fb(score_list,score,t,res)
            
#         score_list.pop()
#         score -= i

def solve_fb(t):
    cash = [[] for _ in range(t+1)]
    cash[0]=[[]]

    for i in range(t+1):
        for pt in [2,3,7]:
            if i - pt >= 0:
                
                for cmb in cash[i-pt]:
                    # print(i, pt)
                    # print(cash[i-pt])
                    if not cmb or pt >= cmb[-1]:
                        cash[i].append(cmb + [pt])
    return cash[t]


for line in sys.stdin:
    t = int(line.strip())
    res = solve_fb(t)
    res=sorted(res)
    # print(res)

    if not res:
        print(f"There are 0 ways to achieve a score of {t}:")
    else:
        if len(res)==1:
            print(f"There is {len(res)} way to achieve a score of {t}:")
        else:
            print(f"There are {len(res)} ways to achieve a score of {t}:")
        for item in res:
            print(" ".join(map(str,item)))




