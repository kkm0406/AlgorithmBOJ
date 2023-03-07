# 과자 나눠주기 S2
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

arr = list(map(int, input().split()))

start = 1
end = max(arr)
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid
    if cnt < m:
        end = mid - 1
    else:
        ans = max(ans, mid)
        start = mid + 1

print(ans)
