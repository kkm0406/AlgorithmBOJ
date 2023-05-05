# 부분수열의 합 S1
import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
result = set()

for i in range(1, len(arr) + 1):
    # 리스트 내에서 원소를 1개~n개를 사용하는 조합
    perms = set(combinations(arr, i))
    for perm in perms:
        # 해당 조합의 합을 add
        result.add(sum(perm))

# 오름차순으로 정렬
result = sorted(list(result))
cnt = 1
# 1부터 시작하여 cnt를 1씩 증가하며 수가 맞는지 확인
for num in result:
    # num이 1씩 증가하지 않는 경우 -> 부분 수열의 합으로 나올 수 없는 자연수
    if num != cnt:
        break
    cnt += 1
print(cnt)
