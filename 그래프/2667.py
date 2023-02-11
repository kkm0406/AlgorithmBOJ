# 단지번호 붙이기 S1
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

arr = [list(input().strip()) for i in range(n)]
visited = [[False] * n for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = []


def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    cnt = 1
    while q:
        x, y = q.popleft()

        for idx in range(4):  # 동서남북 방향에
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == '1':
                # 지도 범위 O, 방문 X, 집이 있으면
                cnt += 1
                visited[nx][ny] = True  # 방문처리
                arr[nx][ny] = '0'  # '0'으로 바꿔줌
                q.append([nx, ny])

    return cnt


for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':  # 집이 있으면 bfs 진행
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)
