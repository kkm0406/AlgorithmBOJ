# 겹치는 건 싫어 S1

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
# 0번째 인덱스부터 시작
l, r = 0, 0
# 해당 숫자가 몇 번 나왔는지 체크
cnt = [0] * (max(arr) + 1)
result = 0

while r < n:
    # r이 가리키는 숫자가 k번 미만으로 나왔으면
    if cnt[arr[r]] < k:
        # 횟수 체크
        cnt[arr[r]] += 1
        # r 증가 -> 범위 늘림
        r += 1
    else:
        # 횟수에서 하나 뺌
        cnt[arr[l]] -= 1
        # l 증가 -> 범위 좁힘
        l += 1

    result = max(result, r-l)

print(result)
