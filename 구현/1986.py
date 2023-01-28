# 체스 S2
import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 최대 깊이 설정
# (대부분의 파이썬의 재귀 최대 깊이의 기본 설정이 1,000회)

input = sys.stdin.readline
n, m = map(int, input().split())
q = list(map(int, input().split()))
k = list(map(int, input().split()))
p = list(map(int, input().split()))
graph = [["o"] * m for _ in range(n)]

dir_kx = [2, 2, -2, -2, 1, -1, 1, -1]  # 나이트 x방향
dir_ky = [1, -1, 1, -1, -2, -2, 2, 2]  # 나이트 y방향

for i in range(1, q[0] * 2, 2):
    nx, ny = q[i] - 1, q[i + 1] - 1
    graph[nx][ny] = "q"

for i in range(1, k[0] * 2, 2):
    nx, ny = k[i] - 1, k[i + 1] - 1
    graph[nx][ny] = "k"

for i in range(1, p[0] * 2, 2):
    nx, ny = p[i] - 1, p[i + 1] - 1
    graph[nx][ny] = "p"


def dfs_q(x, y, v):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] != "p" and graph[x][y] != "k":
        if graph[x][y] != "q":
            graph[x][y] = "x"

        if v == 0:  # 매개변수 v에 따라 한방향 진행
            dfs_q(x + 1, y, 0)
        elif v == 1:
            dfs_q(x - 1, y, 1)
        elif v == 2:
            dfs_q(x, y + 1, 2)
        elif v == 3:
            dfs_q(x, y - 1, 3)
        elif v == 4:
            dfs_q(x + 1, y + 1, 4)
        elif v == 5:
            dfs_q(x + 1, y - 1, 5)
        elif v == 6:
            dfs_q(x - 1, y + 1, 6)
        elif v == 7:
            dfs_q(x - 1, y - 1, 7)
        return True
    return False


for i in range(n):
    for j in range(m):
        if graph[i][j] == "q":  # 퀸이 놓여있다면
            dfs_q(i, j, 0)  # 세번째 매개변수가 방향이 되어 dfs 진행
            dfs_q(i, j, 1)
            dfs_q(i, j, 2)
            dfs_q(i, j, 3)
            dfs_q(i, j, 4)
            dfs_q(i, j, 5)
            dfs_q(i, j, 6)
            dfs_q(i, j, 7)

        elif graph[i][j] == "k":
            for k in range(8):
                nx = i + dir_kx[k]
                ny = j + dir_ky[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] != "p" and graph[nx][ny] != "k" and graph[nx][ny] != "q":
                        graph[nx][ny] = "x"

cnt = 0
for c in graph:
    cnt += c.count("o")

print(cnt)
