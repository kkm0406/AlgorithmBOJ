# MooTube (Silver) G5

import sys
from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())
arr = [[] for i in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])


def bfs(k, v):
    q = deque()
    q.append(v)
    visited = [False] * (n + 1)
    visited[v] = True
    cnt = 0
    while q:
        now = q.popleft()
        for node, cost in arr[now]:
            # 미방문 정점이면서 시작점이 아닐 때
            if not visited[node] and node != v:
                if cost >= k:  # k보다 cost가 크다면
                    cnt += 1
                    q.append(node)
                    visited[node] = True
    return cnt


for _ in range(q):
    k, v = map(int, input().split())
    print(bfs(k, v))
