# 리모콘 G5
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
if m == 0:
    arr = set()
else:
    arr = set(input().split())
ans = abs(100 - int(n))  # 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
for num in range(1000001):  # 이동하려는 채널의 범위는 500,000 이하이지만 채널 자체는 무한대
    for i in str(num):
        if i in arr:  # 현재 숫자 중 고장난 버튼 포함 시
            break
    else:  # else문은 for문이 break 없이 온전하게 완료되면 작동
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)
