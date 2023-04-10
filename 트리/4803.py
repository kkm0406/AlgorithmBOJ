# 트리 G4
import sys
from collections import deque

input = sys.stdin.readline
case = 1


# bfs로 사이클 존재여부 확인
def bfs(i):
    flag = False
    q = deque()
    q.append(i)

    while q:
        now = q.popleft()
        if visited[now]:  # 방문한 정점이면
            flag = True  # 사이클 존재
        visited[now] = True  # 큐에서 뽑았을 때 방문 여부 갱신
        for node in tree[now]:
            if not visited[node]:
                q.append(node)

    return flag


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    tree = [[] for i in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    cnt = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:  # 방문 안한 노드면
            if not bfs(i):  # 연결된 노드 탐색 -> 사이클 여부
                cnt += 1

    if cnt == 0:
        print('Case {}: No trees.'.format(case))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case, cnt))

    case += 1
