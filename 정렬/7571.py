# 점 모으기 S1

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
x, y = [], []

for _ in range(m):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()
# 정렬된 리스트의 중앙값으로 모일 때 최소값
sx, sy = x[m//2], y[m//2]

result = 0

for i in range(m):
    result += abs(sx - x[i]) + abs(sy - y[i])

print(result)
