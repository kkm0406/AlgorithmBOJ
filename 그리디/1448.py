# 삼각형 만들기 S3

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
# 내림차순 정렬
arr = sorted([int(input()) for _ in range(n)], reverse=True)

# 큐로 변환
q = deque(arr)

# 삼각형 -> 최소 3개는 있어야 함
while len(q) >= 3:
    a = q.popleft()
    b = q.popleft()
    c = q.popleft()
    if a < b + c:  # 삼각형 조건
        print(a + b + c)
        exit()
    else:  # 삼각형 x -> 다시 복구
        q.appendleft(c)
        q.appendleft(b)

print(-1)
