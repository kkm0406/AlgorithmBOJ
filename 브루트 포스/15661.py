# 링크와 스타트 S1

import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = sys.maxsize


def check():
    global result
    start, link = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += arr[i][j]
            elif not visited[i] and not visited[j]:
                link += arr[i][j]
    result = min(result, abs(start - link))


def dfs(depth):
    if depth == n:
        check()
        return
    visited[depth] = True
    dfs(depth + 1)
    visited[depth] = False
    dfs(depth + 1)


dfs(0)
print(result)
