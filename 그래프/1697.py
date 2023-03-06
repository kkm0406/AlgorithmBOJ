# 숨바꼭질 S1
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

q = deque()
q.append([n, 0])  # 수빈이 처음위치
visited = [False] * 100001
while q:
    now, cnt = q.popleft()

    if now == k:  # 방문한 점이 동생이 있는 지점이면
        print(cnt)
        break

    for i in (now + 1, now - 1, now * 2):  # 수빈이 이동가능방향
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = True
            q.append([i, cnt + 1])  # 시간+1해서 append
