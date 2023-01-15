# 지구 온난화 S2
import sys

input = sys.stdin.readline().split()
r, c = map(int, input)
arr = [['.'] * (c + 2)]
for i in range(r):
    arr.append(['.'] + list(sys.stdin.readline().strip()) + ['.'])
arr.append(['.'] * (c + 2))

coord = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        cnt = 0
        if arr[i][j] == 'X':
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = i + x
                ny = j + y
                if 0 <= nx < r + 2 and 0 <= ny < c + 2:
                    if arr[nx][ny] == '.':  # 주변의 바다 수 카운트
                        cnt += 1
        if cnt >= 3:
            coord.append([i, j])

for x, y in coord:
    arr[x][y] = '.'

# 출력할 X, Y 시작, 종료 좌표 찾기
start_x = c + 1
end_x = 0
start_y = r + 1
end_y = 0

for row in range(len(arr)):
    if 'X' not in arr[row]:
        continue
    else:
        #섬을 찾으면서 출력할 부분 찾기
        start_y = min(start_y, row)
        end_y = max(end_y, row)
        for col in range(len(arr[row])):
            if arr[row][col] == 'X':
                start_x = min(start_x, col)
                end_x = max(end_x, col)

for row in range(start_y, end_y + 1):
    for col in range(start_x, end_x + 1):
        print(arr[row][col], end='')
    print()
