# 상자넣기 S2

# LIS와 동일한 풀이
import sys

n = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j]+1)


print(max(dp))