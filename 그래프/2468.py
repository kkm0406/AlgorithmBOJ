# 안전 영역 S1
import sys
from collections import deque
import copy

input = sys.stdin.readline
n = int(input())
arr = []
height = set()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * n for i in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    height.update(tmp)  # set으로 모든 높이 저장


def bfs(i, j, h, new_arr):
    q = deque()
    q.append([i, j])
    visited[i][j] = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if new_arr[nx][ny] > h:
                    q.append([nx, ny])
                    new_arr[nx][ny] = 0
                    visited[nx][ny] = True


ans = []
for i in height:
    new_arr = copy.deepcopy(arr)  # 깊은 복사로 새로운 배열 생성
    cnt = 0
    for j in range(n):
        for k in range(n):
            if new_arr[j][k] > i:  # 잠기지 않은 영역이면
                bfs(j, k, i, new_arr)  # bfs 진행
                cnt += 1
    if cnt == 0:  # 아무 지역도 안잠길 경우
        ans.append(1)
    else:
        ans.append(cnt)
    visited = [[False] * n for i in range(n)]  # 방문 초기화

print(max(ans))
