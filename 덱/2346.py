# 풍선 터뜨리기 S3

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
q = deque()
for i in range(n):
    q.append((arr[i], i + 1))
result = []
while q:
    item, idx = q.popleft()
    result.append(idx)
    if item > 0:
        q.rotate(-item + 1)
    elif item < 0:
        q.rotate(-item)

print(*result)
