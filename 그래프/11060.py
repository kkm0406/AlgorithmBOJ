# 점프 점프 S2
import sys

input = sys.stdin.readline

n = int(input())

maze = list(map(int, input().split()))

jump = [1e9] * n

jump[0] = 0

for i in range(n):
    for j in range(1, 1 + maze[i]):
        if i + j < n:
            # 이미 dp 배열에 저장되어 있던 값과,
            # 점프 횟수를 1 증가시킨 값 중 최솟값을
            jump[i + j] = min(jump[i] + 1, jump[i + j])

if jump[n-1] < 1e9:
    print(jump[n-1])
else:
    print(-1)
