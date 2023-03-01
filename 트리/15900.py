# 나무 탈출 S1
# 성원이가 먼저 움직이기 때문에, 움직이는 횟수가 홀수면 성원이 승리
# -> 리프노드에서부터 루트노드까지의 깊이의 합이 홀수일 때 승리
import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n + 1)
depth = [0] * (n + 1)


def dfs(v):
    visited[v] = True

    for i in tree[v]:
        if not visited[i]:
            depth[i] = depth[v] + 1
            dfs(i)


dfs(1)
result = 0
for i in range(2, n + 1):
    if len(tree[i]) < 2:
        result += depth[i]

print('No') if result % 2 == 0 else print('Yes')
