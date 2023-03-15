# 달력 S1
import sys

input = sys.stdin.readline
arr = [0] * 366
n = int(input())

days = []
for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        arr[i] += 1  # 해당 날짜에 일정이 몇개 있는지 추가

w, h = 0, 0
area = 0
for i in range(1, 366):
    if arr[i] != 0:  # 해당 날짜에 일정이 있으면
        w += 1  # 너비 +1
        h = max(h, arr[i])  # 높이는 가장 일정이 많은 날짜
    else:  # 일정이 없으면
        area += w * h  # 그동안 넓이 계산
        w, h = 0, 0  # 너비, 높이 초기화

area += w * h  # for문이 else로 안끝났을 경우 계산 해줘야 함

print(area)
