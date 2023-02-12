# 로봇 청소기 G5
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * m for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited[r][c] = True  # 시작점 방문
cnt = 1  # 시작점 청소

while True:
    flag = False
    for i in range(4):
        d = (d + 3) % 4  # 반시계 90도 회전
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0:
            # 범위 안이고, 청소할 수 있을 때
            if not visited[nx][ny]:
                # 방문 안했으면
                visited[nx][ny] = True
                cnt += 1
                r, c = nx, ny  # 현위치 갱신
                flag = True
                break

    if not flag:  # 네 방향 모두 청소할 수 없으면
        if map[r - dx[d]][c - dy[d]] == 1:
            # 후진했을 때 벽이면 중단
            print(cnt)
            break
        else:  # 후진했을 때 벽이 아니면 위치 갱신
            r, c = r - dx[d], c - dy[d]
