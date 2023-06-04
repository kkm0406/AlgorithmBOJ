# 세로읽기 B1

import sys

input = sys.stdin.readline
arr = []

for i in range(5):
    tmp = input().rstrip()
    for j in range(len(tmp), 15):
        tmp += " "
    arr.append(tmp)

for i in range(15):
    for j in range(5):
        if arr[j][i] == " ":
            continue
        print(arr[j][i], end="")
