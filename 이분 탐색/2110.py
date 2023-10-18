# 공유기 설치 G4
import sys

input = sys.stdin.readline
n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
left, right = 1, arr[-1] - arr[0]  # 가장 오른쪽 집 - 가장 왼쪽 집 => 최대거리
result = 0
while left <= right:
    mid = (left + right) // 2  # 가장 클 수 있는 거리의 중간값
    cur = arr[0]  # 현재 라우터
    cnt = 1
    for i in range(1, len(arr)):  # 두번째 집 ~ 마지막
        if arr[i] - cur >= mid:  # 두 공유기 간 거리는 arr[i] - cur
            cnt += 1  # 공유기 설치
            cur = arr[i]  # 설치 개수 갱신

    if cnt >= c:  # 갯수가 공유기 개수보다 많으면
        result = mid
        left = mid + 1
    elif cnt < c:
        right = mid - 1



print(result)
