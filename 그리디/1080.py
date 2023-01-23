# 행렬 S1
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = [list(map(int, input().strip())) for i in range(n)]
brr = [list(map(int, input().strip())) for i in range(n)]
cnt = 0


def reverse(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            arr[x][y] = not arr[x][y]


for i in range(n - 2):  # 줄바꿈 가능 횟수
    for j in range(m - 2):  # 가로 줄 이동 가능 횟수
        if arr[i][j] != brr[i][j]:  # 숫자 불일치
            reverse(i, j)  # 해당 구역의 숫자 reverse
            cnt += 1

        if arr == brr:
            break
    if arr == brr:
        break

if arr != brr:
    print(-1)
else:
    print(cnt)
