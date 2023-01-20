# 배열 복원하기 S3
import sys

h, w, x, y = map(int, sys.stdin.readline().split())
b = [list(map(int, sys.stdin.readline().split())) for i in range(h + x)]

# 두 배열 모두에 포합되는 경우
# b[i][j] - b[i - x][j - y]
for i in range(x, x + h):
    for j in range(y, w + y):
        if i - x >= 0 and j - y >= 0:
            b[i][j] = b[i][j] - b[i - x][j - y]

# 리스트 슬라이싱
b = b[:h]
for i in b:
    i = i[:w]
    print(*i)
