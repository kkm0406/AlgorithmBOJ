# 문자열 집합 S3
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s, check = [], []
for i in range(n):
    s.append(input().strip())

for i in range(m):
    check.append(input().strip())

cnt = 0
for i in check:
    if i in s:
        cnt += 1

print(cnt)
