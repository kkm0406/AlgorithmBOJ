# 침투 S2

import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for i in range(n)]
visited = [[False] * m for i in range(n)]


def dfs(i, j):
    if board[i][j] == '1':
        return
    visited[i][j] = True

    if 0 <= i + 1 < n and 0 <= j < m:
        if board[i + 1][j] == '0' and not visited[i+1][j]:
            dfs(i + 1, j)

    if 0 <= i - 1 < n and 0 <= j < m:
        if board[i - 1][j] == '0' and not visited[i - 1][j]:
            dfs(i - 1, j)

    if 0 <= i < n and 0 <= j + 1 < m:
        if board[i][j + 1] == '0' and not visited[i][j + 1]:
            dfs(i, j + 1)

    if 0 <= i < n and 0 <= j - 1 < m:
        if board[i][j - 1] == '0' and not visited[i][j - 1]:
            dfs(i, j - 1)


for i in range(m):
    if board[0][i] == '0' and not visited[0][i]:
        dfs(0, i)


for i in range(m):
    if visited[-1][i]:
        print('YES')
        break
else:
    print('NO')
