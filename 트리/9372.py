# 상근이의 여행 S4
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
t = int(input())

cnt, ans = 0, 1e9


def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for i in tree[v]:
        if not visited[i]:
            dfs(i)


for _ in range(t):
    n, m = map(int, input().split())
    tree = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        # 입력한 두 정점을 연결
        tree[a].append(b)
        tree[b].append(a)
    cnt, ans = 0, 1e9
    for i in range(1, n + 1):
        dfs(i)  # i번 정점과 연결된 정점 탐색
        if ans > cnt:  # 최소 개수 계산
            ans = cnt
    print(ans - 1)
