# 피아노 체조 S1
import sys

read = sys.stdin.readline
n = int(read())

arr = list(map(int, read().split()))
dp = [0] * n  # 실수의 횟수를 누적하는 리스트

for i in range(1, n):
    if arr[i - 1] > arr[i]:  # i-1번 난이도가 i번 난이도보다 높다면
        dp[i] = dp[i - 1] + 1  # +1
    else:
        dp[i] = dp[i - 1]  # 아니면 그대로

q = int(read())
for _ in range(q):
    x, y = map(int, read().split())
    print(dp[y - 1] - dp[x - 1])
