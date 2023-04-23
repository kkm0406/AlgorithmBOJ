# 계란으로 계란치기 G5
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
result = 0


def check():
    cnt = 0
    for egg in arr:
        if egg[0] <= 0:
            cnt += 1
    return cnt


def dfs(depth):
    global result
    if depth == n:
        result = max(result, check())
        return
    else:
        # 현재 계란 내구도가 0이하면 다음 계란으로
        if arr[depth][0] <= 0:
            dfs(depth + 1)
        else:
            # 모든 계란이 깨져있는지 여부 확인
            flag = True
            # 현재 계란 내구도가 0보다 클 때 다른 계란들과 부딫힘
            for i in range(n):
                # 현재 계란이 아니고 내구도가 0보다 큰 계란이면
                if i != depth and arr[i][0] > 0:
                    flag = False
                    arr[depth][0] -= arr[i][1]
                    arr[i][0] -= arr[depth][1]
                    dfs(depth + 1)
                    arr[depth][0] += arr[i][1]
                    arr[i][0] += arr[depth][1]
            # 모든 계란이 깨져있을 때
            if flag:
                result = max(result, check())
                return


dfs(0)
print(result)
