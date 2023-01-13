# 2xn 타일링 S3

# n번째는 n-1번째에서 2x1 하나를 추가
# n-2번째에서 1x2 두개를 추가
# dp[n] = dp[n-1]+dp[n-2]

n = int(input())
dp = [0, 1, 2]

for i in range(3, n + 1):
    dp.append((dp[i - 1] + dp[i - 2]) % 10007)

print(dp[n])
