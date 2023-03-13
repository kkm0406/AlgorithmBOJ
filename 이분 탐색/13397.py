# 구간 나누기 2 G4
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0


def divide(x):
    max_x = min_x = arr[0]  # max_x 구간에서 가장 큰 값, min_x: 구간에서 가장 작은 값
    cnt = 1
    for i in range(1, n):
        max_x = max(max_x, arr[i])
        min_x = min(min_x, arr[i])
        if max_x - min_x > x:  # (max_x - min_x)가 mid보다 크면 구간 생성
            cnt += 1
            max_x = min_x = arr[i]

    return cnt


while start <= end:
    mid = (start + end) // 2  # 각 구간의 (최댓값-최솟값) 의 최댓값 중 최솟값
    if divide(mid) <= m:  # 구간 개수가 m보다 작으면 mid 증가
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)
