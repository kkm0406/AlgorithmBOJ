# 봄버맨 S1
import sys

r, c, n = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# 처음 -> 모든 칸 폭탄 -> 1번째 터짐 -> 모든 칸 ->2번째 터짐
# 3초, 7초, 11초, ... -> 1번째 터짐
# 5초, 9초, 13초, ... -> 2번째 터짐
bomb1 = [['O'] * c for i in range(r)]  # 1번째 터졌을 때
bomb2 = [['O'] * c for i in range(r)]  # 두번째 터졌을 때
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'O':
            bomb1[i][j] = '.'
        else:
            for x, y in dir:  # 폭탄 터지는 범위
                nx, ny = i + x, j + y
                if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == 'O':
                    bomb1[i][j] = '.'
                    break
for i in range(r):
    for j in range(c):
        if bomb1[i][j] == 'O':
            bomb2[i][j] = '.'
        else:
            for x, y in dir:
                nx, ny = i + x, j + y
                if 0 <= nx < r and 0 <= ny < c and bomb1[nx][ny] == 'O':
                    bomb2[i][j] = '.'
                    break

if n <= 1:
    for i in arr:
        print("".join(i))
elif n % 2 == 0:
    for i in range(r):
        for j in range(c):
            print('O', end="")
        print()
else:
    if n % 4 == 3:
        for i in bomb1:
            print("".join(i))
    if n % 4 == 1:
        for i in bomb2:
            print("".join(i))
