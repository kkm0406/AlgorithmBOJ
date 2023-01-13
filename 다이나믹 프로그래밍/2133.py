# 타일 채우기 G4

# n-1에서 하나 더 붙이는 경우는 없음
# n-2번째에서 3가지 경우 추가
# 이 때, 짝수번일 때 새로운 두가지 경우가 생김
# dp[n] = 3*dp[n-2] + (2*dp[n-4]+2*dp[n-6]+...+2*dp[0])

n = int(input())
dp = [0] * 1001
dp[0] = 0
dp[1] = 0
dp[2] = 3
for i in range(3, n + 1):
    dp[i] = 3 * dp[i - 2]
    if i % 2 == 0:
        dp[i] += sum(dp[:i - 2]) * 2 + 2

print(dp[n])
