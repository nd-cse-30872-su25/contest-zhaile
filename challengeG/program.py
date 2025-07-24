#! /usr/bin/env python3
# print("Hello world")
import sys
from collections import defaultdict


def make_graph(mat, v):
    graph = defaultdict(list)
    for i in range(v):
        graph[i] = []  
        for j in range(v):
            if mat[i][j] == 1 and i != j:  
                graph[i].append(j)
    return graph

def check_circle(graph):
    visited = set()
    num_discon = 0

    def dfs(v):
        if v in visited:
            return
        visited.add(v)
        for nei in graph[v]:
            dfs(nei)

    for v in graph:
        if v not in visited:
            dfs(v)
            num_discon += 1
    return num_discon

i = 1
for line in sys.stdin:
    if line.strip() == "":
        continue
    v = int(line.strip())
    adg_mat = []
    for _ in range(v):
        row = list(map(int, sys.stdin.readline().strip().split()))
        adg_mat.append(row)
    graph = make_graph(adg_mat, v)
    num = check_circle(graph)
    print(f"System {i} isolated circuits: {num}")
    i += 1
