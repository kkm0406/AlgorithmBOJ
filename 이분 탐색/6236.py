# 용돈 관리 S2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]
# 한번만 인출할 경우 -> r = sum(arr)
l, r = min(arr), sum(arr)
k = 0
while l <= r:
    # 인출할 금액
    mid = (l + r) // 2
    cnt = 1
    # 현재 가진 돈 (처음 인출 시 mid)
    day = mid
    for i in arr:
        # 가진 돈보다 오늘 쓸 돈이 많을 때
        if day < i:
            # mid만큼 새로 인출
            day = mid
            cnt += 1
        # 돈 씀
        day -= i

    # m번 이상 인출 or 인출 금액이 하루에 살기에 적은 경우 (인출 금액이 적음)
    if cnt > m or mid < max(arr):
        l = mid + 1
    # 인출 횟수가 m보다 적거나 작음 (인출 금액이 많음)
    elif cnt <= m:
        r = mid - 1
        k = mid

print(k)
