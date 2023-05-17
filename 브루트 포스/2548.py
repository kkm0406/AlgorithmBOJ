# 대표 자연수 S3

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 오름차순으로 정렬한 리스트에서
# 중앙값을 찾아 중앙값과의 차를 구함
if n == 1:
    print(arr[len(arr) // 2])
else:
    mid1 = arr[len(arr) // 2 - 1]  # ex)n이 6일 때, 2번째 인덱스
    mid2 = arr[len(arr) // 2]  # 3번째 인덱스
    tmp1, tmp2 = 0, 0
    for i in arr:
        tmp1 += abs(i - mid1)
        tmp2 += abs(i - mid2)

    if tmp1 <= tmp2:
        print(mid1)
    else:
        print(mid2)
