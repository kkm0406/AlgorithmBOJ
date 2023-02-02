# LCS 3 G3
# 모든 경우를 반복하며
# 현재의 dp리스트의 원소에 각 비교대상 문자가 같은가,
# 다른가에 따라 이전 dp리스트의 원소의 값을 참조하여 배정
import sys

one = sys.stdin.readline().strip()
two = sys.stdin.readline().strip()
three = sys.stdin.readline().strip()

dp = [[[0] * (len(three) + 1) for i in range(len(two) + 1)] for j in range(len(one) + 1)]

for i in range(1, len(one) + 1):
    for j in range(1, len(two) + 1):
        for k in range(1, len(three) + 1):
            # 3개의 문자가 같을 경우
            if one[i - 1] == two[j - 1] == three[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            # 다를 경우
            else:
                dp[i][j][k] = max(dp[i][j][k - 1], dp[i][j - 1][k], dp[i - 1][j][k])

print(dp[-1][-1][-1])
