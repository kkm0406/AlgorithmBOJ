# Four Squares S3
import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    square = int(i ** (1 / 2))
    min_val = 4
    # n보다 작거나 같은 제곱수를 찾고
    # n-제곱수를 인덱스로 가진 값에 1을 더해주면 된다
    j = 1
    while j ** 2 <= i:
        min_val = min(min_val, dp[i - (j ** 2)])
        j += 1
    dp[i] = min_val + 1

print(dp[n])
