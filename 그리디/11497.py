# 통나무 건너뛰기 S1
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    left = []
    right = []
    for i in range(0, n - 1, 2):
        left.append(l[i])
        right.append(l[i + 1])
    if n % 2 == 0:
        result = left + sorted(right, reverse=True)
    else:
        result = left + [l[-1]] + sorted(right, reverse=True)
    diff = 0
    for i in range(n - 1):
        if abs(result[i] - result[i + 1]) > diff:
            diff = abs(result[i] - result[i + 1])
    if abs(result[0] - result[-1]) > diff:
        diff = abs(result[0] - result[-1])
    print(diff)
