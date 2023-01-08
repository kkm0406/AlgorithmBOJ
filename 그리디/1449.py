# 수리공 항승 S3
import sys

n, l = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0
pos = 0

for i in range(n):
    if arr[i] < pos:
        continue
    pos = arr[i] - 0.5 + l
    cnt += 1

print(cnt)
