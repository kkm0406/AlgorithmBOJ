# 줄어들지 않아 S1

# 2자리일 때 경우의 수: 0->10, 1->9, 2->8, ... => 55
# 3자리수일 때 경우의 수 : 0 -> 55, 1-> 45, 2-> 36, ...
# 이전 인덱스의 누적합 고려
import sys

input = sys.stdin.readline

dp = [[0] * 10 for i in range(65)]  # dp[i][j] -> i번째 자리수 + j숫자 일 때 경우의 수

for i in range(10):
    dp[0][i] = 1

for i in range(1, 65):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][j:])  # i-1번째 자리수의 j번째 숫자부터의 경우의 수의 합

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n][0])
