# 근손실 S3

import sys
from itertools import permutations

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
perms = list(permutations(arr, n))  # 모든 경우의 수를 순열로 계산
cnt = 0
for perm in perms:
    w = 500  # 초기 중량
    for i in perm:
        w -= k
        w += i
        if w < 500:
            break
    else:  # 중량 500이상이면
        cnt += 1

print(cnt)
