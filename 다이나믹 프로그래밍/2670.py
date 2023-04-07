# 연속부분최대곱 S4
import sys

input = sys.stdin.readline
n = int(input())
arr = [float(input()) for i in range(n)]

for i in range(1, n):
    # 현재값과 현재값에 이전 값을 곱한 것 중 max 저장
    arr[i] = max(arr[i], arr[i] * arr[i - 1])

print("{:.3f}".format(max(arr)))
