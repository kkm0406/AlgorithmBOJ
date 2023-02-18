# 예산 S3
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
budget = int(input())

start = 0
end = max(arr)  # 예산 요청 최대값
ans = 0
while start <= end:
    mid = (start + end) // 2
    result = 0  # 예산합
    for i in arr:
        if i >= mid:
            result += mid
        else:
            result += i
    if result <= budget:  # 예산요청합이 국가예산보다 작거나 같으면
        ans = mid
        start = mid + 1
    else:  # 예산요청합이 국가예산보다 크면
        end = mid - 1

print(ans)
