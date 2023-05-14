#개수 세기 B5

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(arr.count(k))