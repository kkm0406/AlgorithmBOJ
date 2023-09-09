# 로봇 시뮬레이션 G5

import sys

input = sys.stdin.readline

dirs = ['N', 'E', 'S', 'W']
dir = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

a, b = map(int, input().split())
n, m = map(int, input().split())
land = [[0] * a for _ in range(b)]
robot = {}

for i in range(n):
    x, y, c = input().split()
    # 로봇별 좌표와 바라보고 있는 방향
    robot[i + 1] = {
        'x': int(x) - 1,
        'y': b - int(y),
        'd': dirs.index(c)
    }
    land[b - int(y)][int(x) - 1] = i + 1  # 로봇의 있는 위치를 표시

for _ in range(m):
    name, order, repeat = input().split()
    name = int(name)
    repeat = int(repeat)
    for _ in range(repeat):  # 반복횟수
        if order == 'F':  # F면 로봇 방향대로 repeat만큼 이동
            land[robot[name]['y']][robot[name]['x']] = 0  # 예전 자리는 0으로 초기화
            d = dirs[robot[name]['d']]  # 로봇이 움직이는 방향
            robot[name]['x'] = robot[name]['x'] + dir[d][1]
            robot[name]['y'] = robot[name]['y'] + dir[d][0]
            if 0 <= robot[name]['x'] < a and 0 <= robot[name]['y'] < b:
                if land[robot[name]['y']][robot[name]['x']] != 0:  # 이동한 자리에 다른 로봇이 있으면
                    print('Robot {} crashes into robot {}'.format(name, land[robot[name]['y']][robot[name]['x']]))
                    exit()
                land[robot[name]['y']][robot[name]['x']] = name  # 현재 로봇이 새로 움직인 자리 표시
            else:  # 범위 벗어난 경우
                print('Robot {} crashes into the wall'.format(name))
                exit()
        elif order == 'L':  # 이동방향 변경
            robot[name]['d'] = (robot[name]['d'] - 1) % 4
        else:  # 이동방향 변경
            robot[name]['d'] = (robot[name]['d'] + 1) % 4

print('OK')
