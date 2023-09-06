# 두 수의 합 S3

import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
left, right = 0, n - 1  # 왼쪽 끝, 오른쪽 끝
cnt = 0
while left < right:
    result = arr[left] + arr[right]
    if result == x:
        cnt += 1
        left += 1
    elif result < x:  # 값을 키워야 함 -> left + 1
        left += 1
    else:  # 값을 줄여야 함 -> right - 1
        right -= 1

print(cnt)
