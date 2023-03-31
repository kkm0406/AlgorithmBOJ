# 돌 게임 2 S4
# n이 짝수이면 마지막 돌을 창영이가 가지게 됨 -> 상근이가 이김
# n이 홀수이면 마지막 돌을 상근이가 가지게 됨 -> 창영이가 이김
import sys

n = int(sys.stdin.readline())
if n % 2 == 0:
    print('SK')
else:
    print('CY')

# ----------------------------------------

# 마지막에 돌을 누가 가져가는지 -> 1이면 상근, 0이면 창영
dp = [0 for i in range(1001)]
dp[1], dp[2], dp[3], dp[4] = 1, 0, 1, 0

for i in range(5, n + 1):
    # 1개 또는 3개를 가져갈 수 있으므로 상대방의 선택지는 i-1 or i-3
    if not dp[i - 1] and not dp[i - 3]:
        dp[i] = 1

if dp[n]:
    print('CY')
else:
    print('SK')
