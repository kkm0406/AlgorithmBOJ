# DNA S4

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

arr.sort()

# 합이 가장 작은 DNA를 찾기 위해
# 우선 문자열 자리 중 가장 많이 사용된 문자로 문자열 구성
# 그 문자열과 비교하여 다른 문자 개수 확인
result = ""
for i in range(m):
    cnt = [0, 0, 0, 0]
    for j in range(n):
        if arr[j][i] == 'A':
            cnt[0] += 1
        elif arr[j][i] == 'C':
            cnt[1] += 1
        elif arr[j][i] == 'G':
            cnt[2] += 1
        elif arr[j][i] == 'T':
            cnt[3] += 1
    if cnt.index(max(cnt)) == 0:
        result += 'A'
    if cnt.index(max(cnt)) == 1:
        result += 'C'
    if cnt.index(max(cnt)) == 2:
        result += 'G'
    if cnt.index(max(cnt)) == 3:
        result += 'T'

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != result[j]:
            cnt += 1

print(result)
print(cnt)
