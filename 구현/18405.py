# 경쟁적 전염 G5
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
s, x, y = map(int, input().split())
virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus.append((arr[i][j], i, j))

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(s, X, Y):
    q = deque(virus)
    count = 0
    while q:
        if count == s:
            break
        for _ in range(len(q)):  # 큐의 길이만큼 반복 -> 매 초마다 증식된 바이러스
            val, x, y = q.popleft()
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = arr[x][y]
                        q.append((arr[nx][ny], nx, ny))
        count += 1
    return arr[X - 1][Y - 1]


virus.sort()  # 처음 정렬하면 숫자가 낮은 순으로 들어오고 bfs 실행
print(bfs(s, x, y))
