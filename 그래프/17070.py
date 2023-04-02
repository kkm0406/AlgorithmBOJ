# 파이프 옮기기 1 G5
# bfs 시간초과, dfs는 pypy로 통과
import sys

input = sys.stdin.readline


def dfs(x, y, dir):
    global cnt

    # (n-1, n-1)에 도착
    if x == n - 1 and y == n - 1:
        cnt += 1

    # 가로 방향 이동인 경우
    if dir == 1:
        # 가로 방향 확인
        if y + 1 < n and arr[x][y + 1] == 0: dfs(x, y + 1, 1)
        # 대각선 방향 확인
        if x + 1 < n and y + 1 < n:
            if arr[x + 1][y + 1] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y] == 0:
                dfs(x + 1, y + 1, 3)

    # 세로 방향 이동인 경우
    elif dir == 2:
        # 세로 방향 확인
        if x + 1 < n and arr[x + 1][y] == 0: dfs(x + 1, y, 2)
        # 대각선 방향 확인
        if x + 1 < n and y + 1 < n:
            if arr[x + 1][y + 1] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y] == 0:
                dfs(x + 1, y + 1, 3)

    # 대각선 방향 이동인 경우
    elif dir == 3:
        # 가로 방향 확인
        if y + 1 < n and arr[x][y + 1] == 0: dfs(x, y + 1, 1)
        # 세로 방향 확인
        if x + 1 < n and arr[x + 1][y] == 0: dfs(x + 1, y, 2)
        # 대각선 방향 확인
        if x + 1 < n and y + 1 < n:
            if arr[x + 1][y + 1] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y] == 0:
                dfs(x + 1, y + 1, 3)


n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
cnt = 0
dfs(0, 1, 1)
print(cnt)

# ----------------------------------------------------------
# dp 풀이
# 0은 가로, 1은 세로, 2는 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

# dir, row, col 순서
dp[0][0][1] = 1

# 처음 (0, 1)에서 가로 방향 시작
# -> 0행의 가로방향 초기화 => 이전 col의 값을 더해줌
for i in range(2, n):
    if arr[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

# 처음 (0, 1)에서 가로 방향 시작이므로 col의 시작은 2부터
for i in range(1, n):
    for j in range(2, n):
        # 현위치가 대각선인 경우 -> (i-1, j)와 (i, j-1)위치에 벽이 없으면
        if arr[i][j] == 0 and arr[i - 1][j] == 0 and arr[i][j - 1] == 0:
            # 이전 가로위치에서 대각선 이동+이전 세로위치에서 대각선 이동+이전 대각선위치에서 대각선 이동
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

        if arr[i][j] == 0:
            # 현위치가 가로인 경우
            # -> (i, j-1): 가로위치에서 이동+대각선위치에서 이동
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            # 현위치가 세로인 경우
            # -> (i-1, j): 세로위치에서 이동+대각선위치에서 이동
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

# 가로위치+세로위치+대각선위치
print(dp[0][n - 1][n - 1] + dp[1][n - 1][n - 1] + dp[2][n - 1][n - 1])
