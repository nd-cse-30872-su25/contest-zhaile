#! /usr/bin/env python3
import sys

def solve_min_path(matrix, row, col):
    dp = [[0] * col for _ in range(row)]
    path = [[-1] * col for _ in range(row)]
    for i in range(row):
        dp[i][0] = matrix[i][0]

    for j in range(1, col):
        for i in range(row):
            prev_rows = [(i - 1 + row) % row, i, (i + 1) % row]
            prev_rows.sort()
            min_val = float('inf')
            for r in prev_rows:
                val = dp[r][j - 1] + matrix[i][j]
                if val < dp[i][j] or dp[i][j] == 0:
                    dp[i][j] = val
                    path[i][j] = r
    min_cost = float('inf')
    last_row = -1
    for i in range(row):
        if dp[i][col - 1] < min_cost:
            min_cost = dp[i][col - 1]
            last_row = i

    result_path = [0] * col
    result_path[-1] = last_row
    for j in range(col - 1, 0, -1):
        result_path[j - 1] = path[result_path[j]][j]
    result_path = [r + 1 for r in result_path]
    return min_cost, result_path



for line in sys.stdin:
    row, col= map(int,line.strip().split())

    matrix = []

    for _ in range(row):
        nums = list(map(int,sys.stdin.readline().strip().split()))
        matrix.append(nums)
    # print(matrix)

    cost, path = solve_min_path(matrix,row,col)

    print(cost)
    print(' '.join(map(str, path)))
