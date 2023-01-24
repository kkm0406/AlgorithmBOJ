# 바이러스 S3
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0] * (n + 1) for i in range(n + 1)]

# 인접 행렬로 구현
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

visited = [False] * (n + 1)
cnt = 0


def dfs(v):
    global cnt
    # 현재 노드 방문 처리
    visited[v] = True
    cnt += 1
    for i in range(1, n + 1):
        # 현재 노드와 연결된 노드가 방문하지 않은 노드이면
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


dfs(1)
print(cnt - 1)
