# 캠프 준비 G5

import sys
from itertools import combinations

input = sys.stdin.readline
n, l, r, x = map(int, input().split())
problems = list(map(int, input().split()))
cnt = 0
# 2개 이상의 문제 조합
for i in range(2, n + 1):
    combs = list(combinations(problems, i))
    for comb in combs:
        comb = sorted(list(comb))
        if l <= sum(comb) <= r and comb[-1] - comb[0] >= x:
            cnt += 1

print(cnt)
