# 보이저 1호 S1
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = ['C' * (m + 2)]
for _ in range(n):
    arr.append(list('C' + input().strip() + 'C'))
arr.append(list('C' * (m + 2)))
pr, pc = map(int, input().split())
direction = ("U", "R", "D", "L")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
left = [1, 0, 3, 2]  # /를 만날 때 바뀌는 방향
right = [3, 2, 1, 0]  # \를 만날 때 바뀌는 방향
result = 0
result_dir = 0

for i in range(4):  # 상하좌우 탐색
    nx, ny = pr, pc  # 처음 시작점
    dir = i
    cnt = 1
    while True:
        # 해당 방향으로 계속 이동
        nx = nx + dx[dir]
        ny = ny + dy[dir]

        # 블랙홀이거나 항성계 벗어나면 break
        if arr[nx][ny] == 'C':
            break

        if arr[nx][ny] == '/':  # /만날 때 방향 바뀜
            dir = left[dir]
        elif arr[nx][ny] == '\\':  # \만날 때 방향 바뀜
            dir = right[dir]
        cnt += 1

        # 시작점으로 돌아오고 처음 출발 방향이랑 같은 경우 무한루프
        if (nx, ny, dir) == (pr, pc, i):
            print(direction[i])
            print("Voyager")
            sys.exit(0)

    if result < cnt:
        result = cnt
        result_dir = i

print(direction[result_dir])
print(result)
