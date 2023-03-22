# 컨베이어 벨트 위의 로봇 G5
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
arr = deque(list(map(int, input().split())))  # 회전을 위해 deque 사용
robot = deque([0] * n)  # 회전을 위해 deque 사용
steps = 0

while True:
    arr.rotate(1)  # 회전
    robot.rotate(1)  # 회전
    robot[-1] = 0  # 로봇 하차

    if sum(robot):  # 벨트위에 로봇이 있으면
        for i in range(n - 2, -1, -1):  # 로봇 한 칸씩 이동
            if robot[i] == 1 and robot[i + 1] == 0 and arr[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                arr[i + 1] -= 1
        robot[-1] = 0  # 로봇 하차

    # 로봇 올릴 수 있으면
    if robot[0] == 0 and arr[0] >= 1:
        robot[0] = 1
        arr[0] -= 1

    steps += 1

    if arr.count(0) >= k:
        print(steps)
        break
