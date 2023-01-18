# 흙길 보수하기 S1
import math
import sys

n, l = map(int, sys.stdin.readline().split())
pool = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

pool.sort(key=lambda x: x[0])
# 널빤지 개수, 널빤지 마지막 위치
cnt, pos = 0, 0
for start, end in pool:
    # 웅덩이 시작점이 널빤지 마지막 위치보다 클수도 있고
    # -> 널빤지 시작점을 웅덩이 시작점으로
    # 널빤지 마지막 위치가 웅덩이 시작점 이후 일수도 있다.
    pos = max(start, pos)
    # 웅덩이 길이
    diff = end - pos
    if (diff + l) % l == 0:
        count = (diff + l - 1) // l
    else:
        count = (diff + l) // l
    cnt += count
    pos += count * l

print(cnt)
