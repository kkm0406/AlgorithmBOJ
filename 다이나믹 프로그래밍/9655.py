# 돌 게임 S5
# i-1번째, i-3번째가 cy턴이면 sk가 이김
import sys

n = int(sys.stdin.readline())
dp = [0 for i in range(1001)]

dp[1], dp[2], dp[3], dp[4] = 1, 0, 1, 0

for i in range(5, n + 1):
    if not dp[i - 1] and not dp[i - 3]:
        dp[i] = 1

if dp[n]:
    print('SK')
else:
    print('CY')
