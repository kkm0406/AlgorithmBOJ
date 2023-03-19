# 풍선 공장 S2
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr) * m
result = 0
while start <= end:
    mid = (start + end) // 2  # 풍선을 부는 시간
    cnt = 0
    for i in arr:
        cnt += mid // i

    if cnt >= m:  # m개보다 많이 불었으면
        result = mid
        end = mid - 1  # 시간 줄임
    else:  # 적게 불었으면
        start = mid + 1  # 시간 추가

print(result)
