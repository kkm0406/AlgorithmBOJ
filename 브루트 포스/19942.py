# 다이어트 G5

import sys

input = sys.stdin.readline
n = int(input())
nutri = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(n)]
result = sys.maxsize
order = []
# menu0, menu1, menu2, menu3 = [], [], [], []
visited = [False] * n
ans = []


def dfs(depth, menu0, menu1, menu2, menu3, total, idx):
    global result, ans
    if depth > n:
        return
    # 최소 비용보다 비쌀 때
    if total > result:
        return
    # 영양분 조건 만족할 때
    if menu0 >= nutri[0] and menu1 >= nutri[1] and menu2 >= nutri[2] and menu3 >= nutri[3]:
        if result > total:
            result = total
            ans = order[:]

    # 현재 인덱스 이후의 인덱스만 고려 -> idx부터 n까지
    for i in range(idx, n):
        order.append(i)
        # 마지막 파라미터로 현재 인덱스+1 -> idx보다 작은 인덱스 선택안함
        dfs(depth + 1, menu0 + arr[i][0], menu1 + arr[i][1], menu2 + arr[i][2], menu3 + arr[i][3], total + arr[i][-1],
            i + 1)
        order.pop()


dfs(0, 0, 0, 0, 0, 0, 0)

if ans:
    print(result)
    ans.sort()
    for i in ans:
        print(i + 1, end=" ")
else:
    print(-1)
