# 도로와 신호등 S4
import sys

N, L = map(int, sys.stdin.readline().split())

pos = 0  # 현재 위치
time = 0  # 경과 시간

for i in range(N):
    d, r, g = map(int, sys.stdin.readline().split())
    time += (d - pos)
    pos = d
    cycle = r + g  # 신호등 주기
    if time % cycle <= r:  # 신호등 주기가 R보다 작으면 빨간불 대기
        waiting = r - (time % cycle)  # 대기시간
        time += waiting

time += (L - pos)  # 마지막 신호등이후 L까지 거리
print(time)
