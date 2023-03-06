import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
l = max(arr)  # 블루레이 개수가 n개일 때 -> arr 최대값
r = sum(arr)  # 블루레이 개수가 1개일 때 -> arr의 합
ans = 1e9
while l <= r:
    mid = (l + r) // 2
    cnt = 0
    sum = 0  # 현재 블루레이 크기
    for i in range(len(arr)):
        if sum + arr[i] > mid:  # i번째 추가 시 mid보다 크면
            cnt += 1  # 분할
            sum = 0  # 초기화
        sum += arr[i]
    if sum:
        cnt += 1

    if cnt > m:  # 블루레이 개수가 m보다 큰 경우 -> 각 블루레이 크기가 작음
        l = mid + 1
    else:
        ans = min(ans, mid)
        r = mid - 1
print(ans)
