# 밑 줄 S1

import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
size = 0
for _ in range(n):
    tmp = input().strip()
    arr.append(tmp)
    size += len(tmp)

size = m - size # '_'로 채워야하는 개수
cnt = len(arr) - 1 # '_'가 들어갈 수 있는 개수
div, mod = divmod(size, cnt) # '_'*div개 만큼 동일하게  채우면 mod개가 남음

# mod개의 '_'가 들어갈 수 있는 조합
combs = list(combinations([i for i in range(1, n)], mod))
ans = []
# 각 경우의 수 구하기
for comb in combs:
    tmp = arr[0]
    for i in range(1, n):
        if i in comb:
            tmp += "_" + "_" * div + arr[i]
        else:
            tmp += "_" * div + arr[i]
    ans.append(tmp)

ans.sort()

print(ans[0])
