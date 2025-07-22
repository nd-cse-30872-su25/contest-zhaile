#! /usr/bin/env python3
# print("Hello world")

import sys

def is_iso(words):
    word1 , word2 = words
    table = {}
    if len(word1) != len(word2):
        return "Not Isomorphic"
    
    for i in range(len(word1)):
        if word1[i] in table:
            if table[word1[i]] != word2[i]:
                return "Not Isomorphic"
        else:
            table[word1[i]]=word2[i]
            table[word2[i]]=word1[i]

    return "Isomorphic"


        

for line in sys.stdin:
    line = line.strip().split()
    # print(line)
    ans=is_iso(line)
    print(ans)

