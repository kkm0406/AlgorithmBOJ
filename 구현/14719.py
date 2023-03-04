# 빗물 G5
import sys

input = sys.stdin.readline
h, w = map(int, input().split())
arr = list(map(int, input().split()))
amount = 0

# 특정 위치에 물이 고이는지 판단
# 맨 왼쪽, 오른쪽 제거
for i in range(1, w - 1):
    left = arr[:i]  # 현위치 기준 왼쪽
    right = arr[i + 1:]  # 현위치 기준 오른쪽
    # 현위치 기준 양 옆에 자신보다 큰 블럭이면 물이 고임

    # 물이 고이는 양은 왼쪽 블럭들의 max, 오른쪽 블럭들의 max
    # 위의 두 수중 min값 만큼 고임
    # ex) 3 0 1 4 -> 현위치 0일 때 min(3, 4)만큼 고여야함
    value = min(max(left), max(right))

    if arr[i] < value:
        amount += value - arr[i]

print(amount)
