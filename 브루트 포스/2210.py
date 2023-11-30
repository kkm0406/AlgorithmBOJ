# 숫자판 점프 S2

import sys
from itertools import permutations

input = sys.stdin.readline

arr = [list(map(int, input().split())) for i in range(5)]
result = set()


def dfs(i, j, num):
    if len(num) == 6:
        result.add(num)
        return

    if 0 <= i + 1 < 5 and 0 <= j < 5:
        dfs(i + 1, j, num + str(arr[i + 1][j]))

    if 0 <= i - 1 < 5 and 0 <= j < 5:
        dfs(i - 1, j, num + str(arr[i - 1][j]))

    if 0 <= i < 5 and 0 <= j + 1 < 5:
        dfs(i, j + 1, num + str(arr[i][j + 1]))

    if 0 <= i < 5 and 0 <= j - 1 < 5:
        dfs(i, j - 1, num + str(arr[i][j - 1]))


for i in range(5):
    for j in range(5):
        dfs(i, j, str(arr[i][j]))

print(len(result))
