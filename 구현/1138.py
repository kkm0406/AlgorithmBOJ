# 한 줄로 서기 S2
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
q = []

for i in range(n - 1, -1, -1):
    if not q:
        q.append(i + 1)
    else:
        if arr[i] == 0:
            q.insert(0, i+1)
        else:
            q.insert(arr[i], i+1)

print(*q)