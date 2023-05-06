# 동전 2 G5
# dp[n]은 가진 동전들로 n원을 만들었을 때 최소가 되는 동전의 개수이다.
# c1, c2, c3라는 가치를 가지는 동전들이 있다고 할 때 dp[n]은
# dp[n-c1], dp[n-c2], dp[n-c3]  셋 중에 가장 개수가 적은 경우를 택하고 하나의 동전의 개수만 더해주면 된다.
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]
dp = [10001] * (k + 1)
dp[0] = 0
for i in arr:
    for j in range(i, k + 1):
        # 코인으로 현재 가치를 만들 수 있다면
        # 현재 가치를 만든 코인의 개수와 j - i를 만든 코인의 개수에서 +1해준 값을 비교
        if dp[j] > 0:
            dp[j] = min(dp[j], dp[j - i] + 1)

print(dp[k]) if dp[k] != 10001 else print(-1)
