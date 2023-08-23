# 나무꾼 이다솜 S1

import sys

input = sys.stdin.readline

n, c, w = map(int, input().split())
arr = [int(input()) for i in range(n)]
ans = 0

# 1부터 가장 긴 나무의 길이까지
for i in range(1, max(arr) + 1):
    result = 0
    # 나무 확인
    for tree in arr:
        # 자른 횟수, 자르고 남은 나무 길이
        cnt, mod = divmod(tree, i)
        if mod:  # 나머지 있으면 자른 나무 수만큼 비용 발생
            tmp = cnt * c
        else:  # 나머지 없으면 자른 나무 수 -1 만큼 비용 발생
            tmp = (cnt - 1) * c
        # 자른 나무 비용
        money = (cnt * i * w) - tmp
        # 자른 나무를 팔 때 이익이 없으면 continue
        if money < 0:
            continue
        # 이익 추가
        result += money

    ans = max(ans, result)

print(ans)
