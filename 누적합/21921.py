# 블로그 S3

import sys

input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0]
for i in range(n):
    dp.append(arr[i] + dp[-1])

# X일 동안의 방문 수 저장 후 내림차순 정렬
result = []
for i in range(x, n + 1):
    result.append(dp[i] - dp[i - x])
result.sort(reverse=True)

# X일 동안 최대 방문자 기간 횟수 세기
cnt = 1
for i in range(1, len(result)):
    if result[i] == result[0]:
        cnt += 1

# 최대 방문자 수가 0일 때
if result[0] == 0:
    print('SAD')
else:
    print(result[0])
    print(cnt)
