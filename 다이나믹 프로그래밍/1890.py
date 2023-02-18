# 점프 S1
import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

# 현 위치로 올수있는 경우 저장
dp = [[0] * n for i in range(n)]
cnt = 0

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:  # 끝에 도달시 종료
            break
        jump = arr[i][j]  # 점프할 수 있는 거리
        if jump + i < n:  # 아래로 점프가능하면
            dp[jump + i][j] += dp[i][j]
        if jump + j < n:  # 오른쪽으로 점프가능하면
            dp[i][j + jump] += dp[i][j]

print(dp[n - 1][n - 1])
