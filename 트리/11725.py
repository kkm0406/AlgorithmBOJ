# 트리의 부모 찾기 S2
import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n + 1)
parent = [0] * (n + 1)


def dfs(node):
    visited[node] = True
    for i in tree[node]:  # node와 연결된 노드 방문
        if not visited[i]:  # 미방문한 노드이면
            visited[i] = True  # 방문 처리
            parent[i] = node  # i 노드의 부모는 node가 됨
            dfs(i)  # 재귀적으로 진행


dfs(1)

for i in range(2, n + 1):
    print(parent[i])
