# 수 고르기 G5

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted([int(input()) for i in range(n)])
left, right = 0, 1  # 투포인터 이용
result = sys.maxsize
while left < n and right < n:
    tmp = arr[right] - arr[left]
    if tmp == m:  # 두 수의 차가 m이면 종료
        print(m)
        sys.exit(0)
    if tmp < m:  # m보다 작으면
        right += 1  # 두 값의 차를 늘려야 함 -> right 이동
    else:  # m보다 크면
        left += 1  # 두 값의 차를 줄여야 함 -> left 이동
        result = min(result, tmp)

print(result)
