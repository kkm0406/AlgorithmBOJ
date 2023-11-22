# 아스키 도형 S1

import sys

input = sys.stdin.readline
size = 0
n, m = map(int, input().split())
arr = [list(input().strip()) for i in range(n)]

for i in range(n):
    # 한 행에서 만난 선분 수
    line = 0
    for j in range(m):
        if arr[i][j] == '/' or arr[i][j] == '\\':
            size += 0.5
            line += 1
        # 만난 선분이 홀수개 -> 도형의 안쪽을 봄
        elif line % 2 == 1 and arr[i][j] == '.':
            size += 1

print(int(size))
