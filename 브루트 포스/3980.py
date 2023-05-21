# 선발 명단 G5

import sys

input = sys.stdin.readline


def dfs(depth, num):
    global result
    if depth == 11:
        result = max(result, num)
    else:
        for i in range(11):  # depth번째 선수 포지션 정하기
            # depth번 선수가 i번 포지션에 뛸 수 있고, i번 포지션에 들어간 선수가 없으면
            if arr[depth][i] != 0 and not visited[i]:
                visited[i] = True
                dfs(depth + 1, num + arr[depth][i])
                visited[i] = False


for _ in range(int(input())):
    arr = [list(map(int, input().split())) for i in range(11)]
    visited = [False] * 11  # 각 포지션 방문 여부
    result = 0
    for i in range(11):
        if arr[0][i] != 0:  # 우선 0번째 선수 포지션 정하기
            visited[i] = True
            dfs(1, arr[0][i])
            visited[i] = False

    print(result)
