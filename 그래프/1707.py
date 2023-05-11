# 이분 그래프 G4
# 이분 그래프: 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프.
# 정점을 방문할 때마다 두 가지 색 중 하나로 칠함
# 인접한 정점이 자신과 동일한 색이면 이분 그래프가 아님
import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def bfs(i):
    q = deque([i])
    while q:
        x = q.popleft()

        for node in arr[x]:  # 인접한 정점 중
            if not visited[node]:  # 미방문 정점은
                q.append(node)  # append
                visited[node] = -1 * visited[x]  # 자신과 다른 색을 칠함
            elif visited[node] == visited[x]:  # 인접한 정점이 자신과 같은 색이면
                return False  # 이분 그래프 아님
    return True


def dfs(i, color):
    visited[i] = color  # 현재 정점의 색을 칠함

    for node in arr[i]:  # 인접한 정점 중
        if not visited[node]:  # 미방분 정점이면
            if not dfs(node, -color):  # 다른 색으로 칠하고 dfs 진행
                return False
        elif visited[i] == visited[node]:  # 인접한 정점과 같은 색이면
            return False  # 이분 그래프 아님
    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    arr = [[] for i in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    # 방문 여부 & 색 체크
    visited = [0] * (v + 1)

    for i in range(1, v + 1):
        if not visited[i]:  # 미방분 정점 탐색
            visited[i] = 1  # 방문 처리
            if not bfs(i):
                print('NO')
                break
        # if not visited[i]:
        #     if not dfs(i, 1):
        #         print('NO')
        #         break
    else:
        print('YES')
