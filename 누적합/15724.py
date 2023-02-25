# 주지수 S1
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * (m + 1) for i in range(n + 1)]

for i in range(n):
    for j in range(m):
        # 2차원 누적합
        # -dp[i][j]는 dp[i][j+1]+dp[i+1][j]의 겹친 부분을 빼는 것
        dp[i + 1][j + 1] = arr[i][j] + dp[i][j + 1] + dp[i + 1][j] - dp[i][j]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # x1-1, y2까지의 부분
    # x2, y1-1까지의 부분을 빼는 과정에서
    # x1-1, y1-1 부분이 두번 빠지기 때문에 한번 더해줌
    ans = dp[x2][y2] + dp[x1 - 1][y1 - 1] - dp[x1 - 1][y2] - dp[x2][y1 - 1]
    print(ans)
