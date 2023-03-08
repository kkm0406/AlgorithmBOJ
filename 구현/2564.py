# 경비원 S1
import sys

input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
x, y = map(int, input().split())
result = 0

# 동근이 위치에서 각 방향까지의 거리 계산
# 동근이와 상점이 마주보고 있는 경우 -> 반시계/시계방향으로 거리 중 최솟값
for i in arr:
    sx, sy = i[0], i[1]
    if x == 1:
        if sx == 1:
            result += abs(y - sy)
        elif sx == 2:
            tmp1 = y + h + sy
            tmp2 = (w - y) + h + (w - sy)
            result += min(tmp1, tmp2)
        elif sx == 3:
            result += y + sy
        else:
            result += (w - h) + sy
    elif x == 2:
        if sx == 1:
            tmp1 = y + h + sy
            tmp2 = (w - y) + h + (w - sy)
            result += min(tmp1, tmp2)
        elif sx == 2:
            result += abs(y - sy)
        elif sx == 3:
            result += y + (h - sy)
        else:
            result += (w - y) + (h - sy)
    elif x == 3:
        if sx == 1:
            result += y + sy
        elif sx == 2:
            result += (h - y) + sy
        elif sx == 3:
            result += abs(y - sy)
        else:
            tmp1 = y + w + sy
            tmp2 = (h - y) + w + (h - sy)
            result += min(tmp1, tmp2)
    elif x == 4:
        if sx == 1:
            result += y + (w - sy)
        elif sx == 2:
            result += (h - y) + (w - sy)
        elif sx == 3:
            tmp1 = y + w + sy
            tmp2 = (h - y) + w + (h - sy)
            result += min(tmp1, tmp2)
        else:
            result += abs(y - sy)

print(result)
