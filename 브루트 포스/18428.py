# 감시 피하기 G5
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(input().split()) for i in range(n)]
teacher = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':  # 선생님의 위치 저장
            teacher.append([i, j])


def bfs():
    for x in teacher:
        for i in range(4):  # 상하좌우 순서대로 이동
            nx, ny = x  # 선생님 위치에서
            while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 'O':
                if arr[nx][ny] == 'S':  # 학생을 만나면
                    return False  # False 리턴
                nx += dx[i]
                ny += dy[i]
    return True  # 학생을 못만나는 경우


flag = False


def dfs(depth):
    global flag
    # 장애물 3개를 설치했으면
    if depth == 3:
        if bfs():  # bfs로 학생위치 탐색
            flag = True
            return
    else:
        # 백트래킹으로 X위치에 장애물 설치
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'X':
                    arr[i][j] = 'O'
                    depth += 1
                    dfs(depth)
                    depth -= 1
                    arr[i][j] = 'X'


dfs(0)
print('YES') if flag else print('NO')
