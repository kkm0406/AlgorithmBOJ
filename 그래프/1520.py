# 내리막길 G3

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 도착지까지 가는 경우의 수는
# 도착 지점이 아닌 임의의 점들에서 도착지점까지 가는 경우를 합한 것과 같음
# -> dp 사용
# 시작지점에서 출발새어 dp테이블이 갱신되지 않은 곳을 만나면
# 해당 지점부터 도착지까지 갈 수 있는 경로의 수를 업데이트
# 이미 갱신되어 있다면 최적해가 되므로 그 값을 그래도 전체 정답에 더함
dp = [[-1] * n for _ in range(m)]


def dfs(x, y):
    # 도착 지점에 도달했다면 1가지 방법 리턴
    if x == m - 1 and y == n - 1:
        return 1

    # 이미 방문한 적이 있으면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for i in range(4):
        # 상하좌우로 이동
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and arr[x][y] > arr[nx][ny]:
            # 이동하는 경우의 수를 더함
            cnt += dfs(nx, ny)

    dp[x][y] = cnt
    return dp[x][y]


result = dfs(0, 0)
print(result)
