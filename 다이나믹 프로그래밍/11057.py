# 오르막 수 S1
# 자리수가 1개인 경우는 당연히 각 숫자가 한 번씩 올 수 있으니 0 ~ 9 까지 한 번씩만 사용되고,
# 자리수가 2개인 경우부터는 표를 기준으로 해당 숫자의 위에 있는 수와 왼쪽에 있는 수를 더한 값이 된다.
# 자리수가 3인 경우에 더 쉽게 확인할 수 있다.
import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for i in range(1001)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(sum(dp[n]) % 10007)
