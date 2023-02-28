# 톱니바퀴 G5
import sys
from collections import deque

input = sys.stdin.readline


def right(idx, d):
    # 더이상 오른쪽 이동 불가
    if idx > 4 or gear[idx - 1][2] == gear[idx][6]:
        return

    if gear[idx - 1][2] != gear[idx][6]:  # 인접 톱니바퀴가 회전 가능하면
        right(idx + 1, -d)  # 오른쪽 이동
        gear[idx].rotate(d)  # 현재 톱니바퀴 회전


def left(idx, d):
    # 더이상 왼쪽 이동 불가
    if idx < 1 or gear[idx][2] == gear[idx + 1][6]:
        return

    if gear[idx][2] != gear[idx + 1][6]:  # 인접 톱니바퀴가 회전 가능하면
        left(idx - 1, -d)  # 왼쪽 이동
        gear[idx].rotate(d)  # 현재 톱니바퀴 회전


gear = {}
for i in range(1, 5):
    gear[i] = deque((map(int, input().strip())))  # rotate 함수를 이용하기 위해 deque 사용

for _ in range(int(input())):
    num, dir = map(int, input().split())

    right(num + 1, -dir)
    left(num - 1, -dir)
    gear[num].rotate(dir)  # rotate()함수를 이용 (양수) -> 오른쪽 회전

ans = 0
for i in range(4):
    ans += gear[i + 1][0] * (2 ** i)

print(ans)
