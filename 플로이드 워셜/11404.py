# 플로이드 G4

import sys

input = sys.stdin.readline
inf = sys.maxsize
n = int(input())
dist = [[inf] * n for i in range(n)]
m = int(input())
for i in range(m):
    a, b, c = map(int, input().split())
    if dist[a - 1][b - 1] > c:
        dist[a - 1][b - 1] = c

for k in range(n):  # 거치는 지점
    for i in range(n):  # 시작점
        for j in range(n):  # 도착점
            if i == j:  # 문제에서 자기자신으로 오는 경우는 없음
                dist[i][j] = 0
            else:
                cost = dist[i][k] + dist[k][j]  # k지점을 경유하는 경로
                dist[i][j] = min(cost, dist[i][j])  # 비교해서 최솟값으로

for i in range(n):
    for j in range(n):
        if dist[i][j] == inf:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
