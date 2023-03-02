# 스타트링크 S1
import sys
from collections import deque

input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
visited = [False] * (f + 1)

q = deque()
q.append([s, 0])  # 현재 층
visited[s] = True
ans = -1

while q:
    floor, cnt = q.popleft()

    if floor == g:  # g층 도착
        ans = cnt
        break

    dir = [u, -d]  # 위로 u층이동, 아래로 d층 이동

    for i in dir:
        if 1 <= floor + i <= f and not visited[floor + i]:
            visited[floor + i] = True
            q.append([floor + i, cnt + 1])

print(ans) if ans != -1 else print('use the stairs')
