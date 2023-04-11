# 컴백홈 S1
import sys

input = sys.stdin.readline
r, c, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0


def dfs(x, y, depth):
    global cnt
    if x == 0 and y == c - 1:
        if depth == k:
            cnt += 1
    else:

        for dx, dy in dir:  # 이동가능한 방향
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문처리
                dfs(nx, ny, depth + 1)  # 재귀적으로 방문
                visited[nx][ny] = False  # 다시 미방문처리


visited[r - 1][0] = True  # 출발위치는 항상 visited
dfs(r - 1, 0, 1)

print(cnt)
