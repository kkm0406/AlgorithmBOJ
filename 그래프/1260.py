# DFS와 BFS S2
import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
# 인접행렬로 그래프 구현
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)


def dfs(v):
    dfs_visited[v] = True
    print(v, end=" ")
    for i in range(1, n + 1):
        if not dfs_visited[i] and graph[v][i] == 1:
            dfs(i)


def bfs(start):
    queue = deque()
    queue.append(start)
    bfs_visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if not bfs_visited[i] and graph[v][i] == 1:
                queue.append(i)
                bfs_visited[i] = True


dfs(v)
print()
bfs(v)
