# 케빈 베이컨의 6단계 법칙 S1
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for j in range(n + 1)]
result = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def bfs(v):
    cnt = 0
    q = deque()
    q.append([v, 0])  # v번 노드와 v번 노드까지의 거리를 저장
    visited[v] = True

    while q:
        x, dist = q.popleft()
        cnt += dist  # 노드 방문할 때 마다 거리 + 1
        for i in range(1, n + 1):
            if graph[x][i] == 1 and not visited[i]:
                q.append([i, dist + 1])
                visited[i] = True

    return cnt


for i in range(1, n + 1):
    visited = [False] * (n + 1)
    result.append(bfs(i))

# 케빈 베이컨 수가 가장 작은 사람이 여러명이어도 find로 하면 가장 앞의 순서를 반환
print(result.index(min(result)) + 1)
