# 소트 G5
# 만약 s가 5라면 현재 위치부터 5개의 위치에서 가장 큰 값을 맨 앞으로 가져올 수 있다
# -> 6개 이상 떨어진 곳의 숫자는 5번의 교환으로 맨 앞으로 가져올 수 없다.
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n - 1):
    if s == 0:
        break

    max, idx = arr[i], i  # 확인하는 원소 중 최대값, 해당 위치
    for j in range(i + 1, min(n, i + 1 + s)):
        # i+1번째 원소부터 옮길 수 있는 최대 idx까지
        if max < arr[j]:  # 탐색한 원소가 max보다 클 경우
            max = arr[j]
            idx = j
    s -= idx - i  # 교체 횟수 감소
    for j in range(idx, i, -1):  # 교환
        arr[j] = arr[j - 1]

    arr[i] = max

print(*arr)
