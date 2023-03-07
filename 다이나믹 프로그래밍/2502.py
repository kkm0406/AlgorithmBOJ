# 떡 먹는 호랑이 S1
import sys

input = sys.stdin.readline
d, k = map(int, input().split())

dp = [[0, 0] for i in range(d + 1)]  # dp[n] -> day1, day2 몇개로 이루어졌는지
dp[1] = [1, 0]
dp[2] = [0, 1]
dp[3] = [1, 1]  # ex) dp[3] = dp[1]+dp[2], dp[4] = dp[3]+dp[2] = dp[2] +dp[1] + dp[1]
for i in range(4, d + 1):
    dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]

x, y = dp[-1][0], dp[-1][1]  # 최종 day1, day2 개수
a = 1  # day1준 떡의 개수
# day1개수 * day1 떡의 개수 + day2개수 * day2 떡의 개수 = k
# -> day1 떡의 개수, day2 떡의 개수 찾기
while True:
    result = k - (x * a)
    if result % y == 0:
        print(a)
        print(result // y)
        break
    a += 1
