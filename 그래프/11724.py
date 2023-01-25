# 연결 요소의 개수 S2
import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())

graph = [[0] * (n + 1) for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1


def bfs(x):
    q = deque([x])

    visited[x] = True

    while q:
        v = q.popleft()
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i] == 1:
                q.append(i)
                visited[i] = True


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:  # 아직 방문을 안한 정점이면
        bfs(i)  # BFS 진행
        cnt += 1
print(cnt)
