# 카드 구매하기 2 S1
# dp[i] = 카드 i개 구매하는 최대 가격 , p[k] = k개가 들어있는 카드팩 가격
# p[1] + dp[i-1]/ p[2] + dp[i-2]/ p[3] + dp[i-3]/ p[i] + dp[0]
# -> 카드를 i개 구매하는 최소 비용
import sys

input = sys.stdin.readline
n = int(input())
card = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = card[1]

for i in range(1, n + 1):
    dp[i] = card[i]
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + card[j])

print(dp[n])
