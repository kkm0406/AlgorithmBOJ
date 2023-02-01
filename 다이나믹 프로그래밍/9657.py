# 돌 게임 3 S3
# N번째 돌을 가져가면 이김
# N-1, N-3, N-4번째에 상대턴이 1개라도 이기면 이길 수 있음
# 상대턴으로 넘길 수 있는 경우의 수가 있으면
# 그 경우의 수를 놓아 이길 수 있기 떄문
import sys

n = int(sys.stdin.readline())

dp = [0] * 1001

dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1

for i in range(5, n + 1):
    if not dp[i - 1] or not dp[i - 3] or not dp[i - 4]:
        dp[i] = 1

if dp[n]:
    print('SK')
else:
    print('CY')
