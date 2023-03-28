# 트리와 쿼리 G5
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, r, q = map(int, input().split())
tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

children = [0] * (n + 1)

cnt = 0


def dfs(x):
    children[x] = 1
    for node in tree[x]:  # 연결된 정점중에
        if children[node] == 0:  # 방문하지 않은 정점이 있으면
            dfs(node)  # 탐색
            children[x] += children[node]  # 방문한 정점의 서브트리의 개수를 더함


# dfs로 탐색하면서 각 정점에 대한 서브트리의 수를 리스트에 저장
dfs(r)

for i in range(q):
    print(children[int(input())])
