# ABCDE G5

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] * n for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False] * n
flag = False


# A-B-C-D-E: 시작노드부터 4개의 노드 탐색 시 성공
def dfs(start, depth):
    global flag
    visited[start] = True
    if depth == 5:  # 탐색한 노드 개수가 5개면 성공
        flag = True
        return
    for i in arr[start]:  # 다음 노드 탐색
        if not visited[i]:
            dfs(i, depth + 1)

    visited[start] = False


# i번째 노드부터 dfs
for i in range(n):
    dfs(i, 1)
    if flag:
        break

if flag:
    print(1)
else:
    print(0)
