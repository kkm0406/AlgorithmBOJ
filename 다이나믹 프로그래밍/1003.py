# 피보나치 함수 S3
import sys

input = sys.stdin.readline
dp = [[0, 0] for i in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]
for i in range(2, 41):
    # i번째 수의 0 호출 횟수: i-1, i-2의 0 호출 횟수의 합
    # 1 호출 횟수: i-1, i-2의 1 호출 횟수의 합
    dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]

for _ in range(int(input())):
    print(*dp[int(input())])
