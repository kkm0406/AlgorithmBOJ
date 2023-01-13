# 2×n 타일링 2 S3

# n번째는 n-1번째에서 2x1 하나를 추가
# n-2번째에서 2x2 하나 or 1x2 두개 추가
# dp[n] = dp[n-1]+2*dp[n-2]

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007

print(dp[n])
