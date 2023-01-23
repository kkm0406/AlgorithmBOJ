# 부분수열의 합 S2
import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    # 해당 수열에서 가능한 모든 조합을 구함
    comb = combinations(arr, i + 1)
    for j in comb:
        if sum(j) == s:  # 해당 조합의 합 == s
            cnt += 1
print(cnt)
