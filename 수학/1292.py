# 쉽게 푸는 문제 B1
import sys

a, b = map(int, sys.stdin.readline().split())
arr = [0]
for i in range(1, b+1):
    for j in range(i):
        arr.append(i)
print(sum(arr[a:b+1]))
# for i in
# for i in range(b):