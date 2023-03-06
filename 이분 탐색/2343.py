# 기타 레슨 S1
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)  # 최소 블루레이의 크기 ( n==m일 때 -> max(arr))
end = sum(arr)  # 최대 블루레이의 크기 (m==1일 때)
result = sum(arr)
while start <= end:
    mid = (start + end) // 2  # 블루레이의 크기
    if mid < max(arr):  # 블루레이 크기가 전체 합보다 작으면
        start = mid + 1
        continue
    cnt = 1  # 블루레이 개수
    blue_ray = 0  # 블루레이 크기
    for i in arr:
        if blue_ray + i <= mid:  # i를 추가했을 때 mid를 넘지 않으면
            blue_ray += i
        else:  # i추가 시 mid를 초과하면
            cnt += 1  # 블루레이 개수 +1
            blue_ray = i

    if cnt <= m:  # 블루레이 개수가 m보다 작으면
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1

print(result)
