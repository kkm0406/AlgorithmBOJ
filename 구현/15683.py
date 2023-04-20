# 감시 G4

import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv = []
result = sys.maxsize
for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            cctv.append([arr[i][j], i, j])

cctv.sort(reverse=True)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 각 CCTV 번호별 감시할 수 있는 방향
moves = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]


def check(tmp, move, x, y):
    # 해당 CCTV 채널이 감시할 수 있는 방향
    for i in move:
        # CCTV 존재 위치에서
        nx, ny = x, y
        while True:
            # 감시방향으로 계속 진행하면서
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 만나면 중지
                if tmp[nx][ny] == 6:
                    break
                # 빈칸이면 확인
                elif tmp[nx][ny] == 0:
                    tmp[nx][ny] = -1
            else:
                break


# 백트래킹으로 모든 CCTV가 감시하는 칸 찾기
def dfs(depth, arr):
    global result
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt += 1
        result = min(result, cnt)
    else:
        # 존재하는 CCTV의 채널과 위치
        channel, x, y = cctv[depth]
        # 매 방향 조합이 감시하는 칸을 체크해야하기 때문에 리스트 복사
        tmp = copy.deepcopy(arr)
        # 해당 CCTV의 채널이 감시하는 방향
        for move in moves[channel]:
            check(tmp, move, x, y)
            dfs(depth + 1, tmp)
            tmp = copy.deepcopy(arr)


dfs(0, arr)
print(result)
