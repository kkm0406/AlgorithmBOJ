# 공통 부분 문자열 G5
import sys

input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()
dp = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
ans = 0
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:  # 같은 문자면
            dp[i][j] = dp[i - 1][j - 1] + 1  # 이전 공통 부분 문자열 길이+1.
            if ans < dp[i][j]:
                ans = dp[i][j]

print(ans)
