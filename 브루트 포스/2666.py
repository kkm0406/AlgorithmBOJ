# 벽장문의 이동 G5

import sys

input = sys.stdin.readline

n = int(input())
open = list(map(int, input().split()))
N = int(input())
arr = [-1] + [int(input()) for i in range(N)]
door = []  # 벽장의 상태
for i in range(n + 1):
    if i in open:  # 열린 벽장
        door.append(0)
    else:
        door.append(1)
result = sys.maxsize


def check(x, cnt, door):
    global result
    if x == N + 1:
        result = min(result, cnt)
        return
    now = arr[x]  # 현재 위치
    # 벽장을 왼쪽으로 이동하는 경우
    for i in range(now, 0, -1):
        if door[i] == 0:  # 벽장이 열려있을 때
            tmp = door[:]  # 리스트 전체를 가져옴
            tmp[i], tmp[now] = tmp[now], tmp[i]  # 위치 교환
            check(x + 1, cnt + abs(now - i), tmp)  # 재귀적으로 탐색
    # 벽장을 오른쪽으로 이동하는 경우
    for i in range(now, n + 1):
        if door[i] == 0:
            tmp = door[:]
            tmp[i], tmp[now] = tmp[now], tmp[i]
            check(x + 1, cnt + abs(now - i), tmp)


check(1, 0, door)
print(result)
