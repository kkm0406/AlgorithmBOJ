# 알약 G5
import sys

input = sys.stdin.readline
dp = [[0] * 31 for i in range(31)]
# i 는 w의 개수, j는 h의 개수로 dp[i][j] 는 w i 개 h j개로 만들 수 있는 경우의 수

# w가 없고 h 만 남아있다면 어차피 경우의 수는 h를 선택하는 방법 밖에 없기 때문에
# dp[0][h] 를 1로 초기화 해준다.
for i in range(1, 31):
    dp[0][i] = 1

for w in range(1, 31):
    for h in range(30):
        if h == 0:
            # h가 하나도 없을 때 w를 하나먹으면 h가 하나 무조건 생긴다.
            dp[w][h] = dp[w - 1][h + 1]
        else:
            # 반쪽 자리 j 가 하나라도 있으면
            # h 를 먹을 때와  w 를 먹을 때 두가지 경우를 구해서 더해준다.
            dp[w][h] = dp[w][h - 1] + dp[w - 1][h + 1]
while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][0])
