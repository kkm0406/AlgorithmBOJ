# 노드사이의 거리 G5

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])


def bfs(s, e):
    q = deque()
    # 현재 노드와 이동거리를 deque에 저장
    q.append([s, 0])
    visited = [False] * (n + 1)
    visited[s] = True
    while q:
        x, val = q.popleft()
        if x == e:
            return val

        for node in tree[x]:
            if not visited[node[0]]:
                # 연결된 노드와 해당 노드까지의 거리를 더해 저장
                q.append([node[0], val + node[1]])
                visited[node[0]] = True


for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e))
