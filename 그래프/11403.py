# 경로 찾기 S1
# 플로이드 와샬
# i는 거쳐가는 노드, j는 시작 노드, k는 도착 노드 순으로 반복문을 작성
# j -> i와 i -> k가 존재하면 j -> k를 이어줌
import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
arr = [[0] * n for i in range(n)]

for i in range(n):  # i 노드를 거침
    for j in range(n):  # j노드에서 시작
        for k in range(n):  # k노드로 도착
            if graph[j][i] == 1 and graph[i][k] == 1:
                graph[j][k] = 1

for i in graph:
    print(*i)
