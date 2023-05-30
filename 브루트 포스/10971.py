# 외판원 순회 2 S2

import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
result = sys.maxsize
visited = [False] * n


# 출발지점, 현재지점, 비용, depth
def tsp(start, now, val, depth):
    global result
    if depth == n - 1:
        # 현재지점에서 출발지점까지 비용이 있으면 추가함
        if arr[now][start] != 0:
            val += arr[now][start]
            result = min(result, val)
    else:
        for i in range(n):
            # 미방문지점, arr[i][i]가 아닐 때
            if not visited[i] and arr[now][i] != 0:
                visited[i] = True
                tsp(start, i, val + arr[now][i], depth + 1)
                visited[i] = False


# 출발 시작할 지점
for i in range(n):
    visited[i] = True
    # 출발지점, 현재지점, 비용, depth
    tsp(i, i, 0, 0)
    visited[i] = False

print(result)
