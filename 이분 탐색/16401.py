# 과자 나눠주기 S2
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

arr = list(map(int, input().split()))

start = 1  # zero division error -> 1로 설정
end = max(arr)  # 과자 최댓값
ans = 0
while start <= end:
    mid = (start + end) // 2  # 나누어줄 과자 크기
    cnt = 0
    for i in arr:
        cnt += i // mid  # 나누어줄 수 있는 과자 개수 연산

    # 나누어줄 수 있는 과자 개수와 조카 수 비교하면서 이분탐색 진행
    if cnt < m:
        end = mid - 1
    else:
        ans = max(ans, mid)
        start = mid + 1

print(ans)
