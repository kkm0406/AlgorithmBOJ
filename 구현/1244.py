# 스위치 켜고 끄기 S4

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
for _ in range(int(input())):
    gender, idx = map(int, input().split())
    if gender == 1:
        for i in range(n):
            if (i + 1) % idx == 0:
                arr[i] = 1 - arr[i]
    else:
        idx -= 1
        arr[idx] = 1 - arr[idx]
        l, r = idx - 1, idx + 1
        while 0 <= l and r < n:
            if arr[l] == arr[r]:
                arr[l] = 1 - arr[l]
                arr[r] = 1 - arr[r]
                l -= 1
                r += 1
            else:
                break

for i in range(n):
    print(arr[i], end=" ")
    if (i + 1) % 20 == 0:
        print()
