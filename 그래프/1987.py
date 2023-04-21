# 알파벳 G4
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(list(input()))
alpha = set()  # 지나온 알파벳 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0


def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):  # 상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        # 알파벳 중복없고 범위 안에 있으면
        if 0 <= nx < r and 0 <= ny < c and not arr[nx][ny] in alpha:
            alpha.add(arr[nx][ny])
            dfs(nx, ny, cnt + 1)
            alpha.remove(arr[nx][ny])


# 시작 위치 알바펫 추가
alpha.add(arr[0][0])
dfs(0, 0, 1)
print(result)
