# 랜선 자르기 S2
import sys

input = sys.stdin.readline
k, n = map(int, input().split())
arr = [int(input()) for i in range(k)]

start = 1  # zero division error떠서 1로 초기화
end = max(arr)  # 랜선 길이 최대값
ans = 0

while start <= end:
    mid = (start + end) // 2  # mid 길이 기준으로 자름
    result = 0  # 랜선 자른 개수
    for i in arr:
        result += (i // mid)

    if result < n:  # 필요개수보다 모자라면
        end = mid - 1  # 자르는 길이 줄임
    else:
        ans = mid
        start = mid + 1

print(ans)
