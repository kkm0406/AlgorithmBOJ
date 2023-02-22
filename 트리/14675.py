# 단절점과 단절선 S1
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())
for i in range(q):
    t, k = map(int, input().split())
    if t == 1:  # 정점 중 리프노드가 아니면 모두 단절점
        if len(tree[k]) >= 2:
            print('yes')
        else:  # tree[k]의 길이가 1이하면 리프노드
            print('no')
    elif t == 2:  # 트리이므로 모든 간선은 단절선
        print("yes")
