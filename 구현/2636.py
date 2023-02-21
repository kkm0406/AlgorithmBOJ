# 치즈 G4
# 외부 공기와 접촉한 치즈만을 녹이려면, 값이 0인 부분에 대해서만 BFS를 진행
# 판의 가장자리에는 치즈가 놓여 있지 않다는 조건이 주어졌으므로
# 가장자리의 어느 한 지점에서부터 탐색을 진행
# 상하좌우의 좌표 (nx, ny)를 각각 살피고,
# (nx, ny)에 놓인 값이 0이라면 공기라는 것이므로 계속 탐색하기 위해 q에 넣는다.
# (nx, ny)에 놓인 값이 1이라면 공기와 맞닿은 치즈라는 것이므로 녹이기 위해 melt에 넣는다.
# 이 상황에서 바로 녹여버리면 (nx, ny) 주변의 치즈가 (nx, ny)를 공기로 인식해버리기 때문이다.
# 한 타임에 한 번, 공기와 맞닿은 치즈를 한꺼번에 녹여야 한다.
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
ans = 0
time = 1
for i in arr:
    ans += sum(i)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    melt = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if arr[nx][ny] == 0:
                    q.append([nx, ny])
                elif arr[nx][ny] == 1:
                    melt.append([nx, ny])

    # q가 비면 모든 공기를 탐색했다는 것이므로
    # 이제 melt에서 좌표를 꺼내 공기와 맞닿은 치즈를 모두 녹여준다.
    for x, y in melt:
        arr[x][y] = 0

    return len(melt)


while True:
    visited = [[0] * m for i in range(n)]
    cnt = bfs(0, 0)
    ans -= cnt
    if ans == 0:
        print(time)
        print(cnt)
        break
    time += 1
