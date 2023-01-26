# 결혼식 S2
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False] * (n + 1)

cnt = 0


def bfs(x):
    global cnt
    q = deque()
    q.append([x, 0])  # 1번 노드와의 거리를 저장
    visited[x] = True

    while q:
        v, dist = q.popleft()
        if dist <= 2:  # 친구의 친구 (dist==2)까지 초대
            cnt += 1
        for i in range(n + 1):
            if graph[v][i] == 1 and not visited[i]:
                q.append([i, dist + 1])  # 새로운 노드까지의 거리: dist+1
                visited[i] = True


bfs(1)

print(cnt - 1)  # 자기 자신 제외
