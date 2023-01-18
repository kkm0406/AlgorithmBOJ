# 모든 순열 S3
from itertools import permutations
n = int(input())
arr = [i for i in range(1, n+1)]
perm = list(map(list, permutations(arr, n)))

for i in perm:
    print(*i)