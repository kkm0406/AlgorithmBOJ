# 숨바꼭질 S1

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs(start):
    visited[start] = 1
    q = deque([start])

    while q:
        now = q.popleft()

        for node in arr[now]:
            if visited[node] == 0:
                visited[node] = visited[now] + 1
                q.append(node)


bfs(1)
dist = max(visited)
cnt = 0

for i in range(1, n + 1):
    if dist == visited[i]:
        result.append(i)

print(result[0], dist - 1, len(result))
