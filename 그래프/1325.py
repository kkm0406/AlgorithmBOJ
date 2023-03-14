# 효율적인 해킹 S1
# pypy로 제출
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
result = {}
for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)  # a가 b를 신뢰할 때 -> b해킹 시 a 해킹 => 단방향 연결


def bfs(v):
    q = deque()
    q.append(v)
    visited = [False] * (n + 1)
    visited[v] = True
    cnt = 1

    while q:
        x = q.popleft()
        for i in arr[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt


result = [0]
for i in range(1, n + 1):
    result.append(bfs(i))  # 해킹할 수 있는 컴퓨터 수 bfs로 탐색

num = max(result)
for i in range(1, n + 1):
    if result[i] == num:
        print(i, end=" ")
