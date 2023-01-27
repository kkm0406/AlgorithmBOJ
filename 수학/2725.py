# 보이는 점의 개수 S2
# (0,0)에서 보이지 않으려면 직선의 기울기가 달라야 한다.
# 4/2나 6/3은 약분하면 둘 다 기울기가 2로 똑같다.
# 따라서 분자와 분모의 최대공약수가 1인 값들을 찾아내면 된다.
import sys

c = int(sys.stdin.readline())

dp = [0] * 1001
dp[1] = 3


def gcd(i, j):
    if j == 0:
        return i
    return gcd(j, i % j)


for i in range(2, 1001):
    cnt = 0
    for j in range(1, i + 1):
        if i == j:
            continue
        if gcd(i, j) == 1:
            cnt += 2
    dp[i] = dp[i - 1] + cnt

for _ in range(c):
    n = int(sys.stdin.readline())
    print(dp[n])
