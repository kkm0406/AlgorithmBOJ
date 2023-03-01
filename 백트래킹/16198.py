# 에너지 모으기 S1
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = 0


def dfs(result):
    global ans
    if len(arr) == 2:  # 에너지 구슬을 다 모았을 때
        if ans < result:
            ans = result
        return
    for i in range(1, len(arr) - 1):
        tmp = arr[i - 1] * arr[i + 1]  # i번째 구슬 제거시 에너지
        w = arr[i]
        arr.pop(i)  # 해당 에너지 구슬 제거
        dfs(result + tmp)  # 에너지 구슬 제거 후 재귀적 탐색
        arr.insert(i, w)  # 에너지 구슬 추가


dfs(0)
print(ans)
