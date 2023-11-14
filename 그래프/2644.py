# 촌수계산 S2
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
s, e = map(int, input().split())
m = int(input())

arr = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs(start):
    visited = [0] * (n + 1)
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if now == e:
            break
        for node in arr[now]:
            # 자식노드에 도착하는 경우
            if visited[node] == 0:
                # 부모노드의 촌수 + 1
                visited[node] = visited[now] + 1
                q.append(node)

    return visited[e]


result = bfs(s)
print(result if result > 0 else -1)
