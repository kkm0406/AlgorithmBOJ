# 동전 1 G5
# 가치의 합이 i(1 <= i <= k)원이 되는 경우의 수를 구하는 부분 문제로 세분화 함
# ex) 1, 2, 5원 동전으로 10원을 만드는 경우
# 1. 1원짜리 동전만 사용해서 만드는 경우 고려
# -> dp[1] = dp[2] = ... = dp[10] = 1
# 2. 1원, 2원을 사용해서 만드는 경우
# -> 2원을 포함시키지 않는 방법 = 1원만 사용하는 경우는 이미 계산함. 이 값이 dp[k]
# -> 2원을 포함하는 방법인 dp[k-2]를 더하면 됨
# w원짜리 동전을 추가할 때 dp[k] += dp[k-w] 점화식 성립
import sys

n, k = map(int, sys.stdin.readline().split())
value = [int(sys.stdin.readline()) for _ in range(n)]
value.sort()
dp = [0] * (k + 1)
# dp[i] -> i원을 만들 때 가능한 경우의 수
# dp[0] -> 동전 하나를 사용하는 경우 (coin이 3일 때,
# dp[3 - 3] = 1로 맞춰줌으로써 0원에서 3원을 더해 3원을 만드는 경우라고 생각)
dp[0] = 1
for val in value:
    for j in range(val, k + 1):
        dp[j] = dp[j] + dp[j - val]

print(dp[k])
