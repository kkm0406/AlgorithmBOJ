# 히오스 프로게이머 S1
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]

# 목표레벨 T는 k를 여러명에 나눴을 때 가장 큰 mid값
start = min(arr)
end = min(arr) + k  # 한명에게 몰아줄 때
result = 0
while start <= end:
    mid = (start + end) // 2  # 팀 목표레벨
    total = 0  # 팀이 올린 총 레벨
    for i in arr:
        if mid > i:  # 팀 목표레벨이 i보다 크면
            # 팀 목표레벨이 mid일 때, mid-i만큼 i의 레벨을 올림
            total += (mid - i)

    if total > k:
        end = mid - 1
    else:
        start = mid + 1
        result = max(result, mid)

print(result)
