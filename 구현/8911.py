# 거북이 S3
import sys

input = sys.stdin.readline

# NESW
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(int(input())):
    ctrls = list(input().rstrip())
    dir = 0
    # min: 음의 좌표, max: 양의 좌표
    x, y, min_x, min_y, max_x, max_y = 0, 0, 0, 0, 0, 0
    result = 0
    for ctrl in ctrls:
        if ctrl == 'F':
            # 한 칸 앞으로
            x += dx[dir]
            y += dy[dir]
        elif ctrl == 'B':
            # 한 칸 뒤로
            x -= dx[dir]
            y -= dy[dir]
        elif ctrl == 'R':
            # 오른쪽으로 90도 회전
            if dir == 3:
                dir = 0
            else:
                dir += 1
        elif ctrl == 'L':
            # 왼쪽으로 90도 회전
            if dir == 0:
                dir = 3
            else:
                dir -= 1
        # min: 음의 좌표, max: 양의 좌표
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        result = max(result, (max_x - min_x) * (max_y - min_y))
    print(result)
