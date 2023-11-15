# 절사평균 S3

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [float(input()) for i in range(n)]
arr.sort()
avg1 = deque(arr)
avg2 = deque(arr)
tmp1, tmp2 = [], []
for _ in range(k):
    avg1.pop()
    avg1.popleft()
    tmp1.append(avg2.pop())
    tmp2.append(avg2.popleft())

for i in range(len(tmp1)):
    tmp1[i] = avg2[-1]
    tmp2[i] = avg2[0]

result1 = sum(avg1) / len(avg1)
result2 = (sum(avg2) + sum(tmp1) + sum(tmp2)) / n

print("%.2f" % (result1 + 0.00000001))
print("%.2f" % (result2 + 0.00000001))
