# 캡틴 이다솜 S1
import sys

input = sys.stdin.readline
n = int(input())
arr = []
num = 0
i = 1

while n > num:
    num += (i * (i + 1)) // 2
    arr.append(num)
    i += 1

dp = [1e9 for i in range(n + 1)]
for i in range(1, n + 1):  # 1부터 n까지의 대포알 수로 만들 수 있는 사면체 탐색
    for a in arr:
        if a == i:  # 현재 대포알의 수로 사면체를 만들 수 있다면
            dp[i] = 1
            break
        elif a > i:  # 대포알 개수로 사면체를 만들 수 없을 때
            break
        # ex) 현재 i개의 대포알을 사용한 사면체의 개수 vs i개의 대포알에서 a개의 대포알을 빼서 생긴 사면체를 하나 더한 경우
        dp[i] = min(dp[i], 1 + dp[i - a])

print(dp[n])
