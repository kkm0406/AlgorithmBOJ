# 내려가기 G5
import sys

input = sys.stdin.readline
n = int(input())

# 메모리 제한으로 2*3배열 선언
min_dp = [[0, 0, 0] for _ in range(2)]
max_dp = [[0, 0, 0] for _ in range(2)]

for i in range(n):
    arr = list(map(int, input().split()))

    # 0번은 그 전에 선택한 경우가 0번, 1번
    max_dp[1][0] = max(max_dp[0][0], max_dp[0][1]) + arr[0]
    min_dp[1][0] = min(min_dp[0][0], min_dp[0][1]) + arr[0]

    # 1번은 그 전에 선택한 경우가 0, 1, 2번
    max_dp[1][1] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + arr[1]
    min_dp[1][1] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + arr[1]

    # 2번은 그 전에 선택한 경우가 1번, 1번
    max_dp[1][2] = max(max_dp[0][1], max_dp[0][2]) + arr[2]
    min_dp[1][2] = min(min_dp[0][1], min_dp[0][2]) + arr[2]

    # 메모리 제한때문에
    # i번째 배열에 영향을 주는 것은 i-1째 값이므로
    # 2*3의 2차원 배열을 계속 갱신
    max_dp[0][0], max_dp[0][1], max_dp[0][2] = max_dp[1][0], max_dp[1][1], max_dp[1][2]
    min_dp[0][0], min_dp[0][1], min_dp[0][2] = min_dp[1][0], min_dp[1][1], min_dp[1][2]

print(max(max_dp[-1]), min(min_dp[-1]))
