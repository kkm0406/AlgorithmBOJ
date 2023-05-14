# 완전제곱수 B2
import math
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
arr = []
for i in range(n, m + 1):
    if int(i ** 0.5) ** 2 == i:
        arr.append(i)

if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
