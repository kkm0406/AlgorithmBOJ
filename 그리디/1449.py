# 수리공 항승 S3
import sys

n, l = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0
pos = 0  # 테이프 위치

for i in range(n):
    if arr[i] < pos:
        # 물이 새는 위치 < 테이프 현재 위치
        # -> 이미 붙인 곳
        continue
    pos = arr[i] - 0.5 + l  # 테이프 위치 초기화
    cnt += 1

print(cnt)
