# 뱀과 사다리 게임 G5
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
ladders = {}
snakes = {}
for i in range(n):
    a, b = map(int, input().split())
    ladders[a] = b  # 사다리로 이동
for i in range(m):
    a, b = map(int, input().split())
    snakes[a] = b  # 뱀을 이용해 이동
cnt = [0] * 101
visited = [False] * 101
visited[1] = True
q = deque([1])  # 1번부터 시작

while q:
    x = q.popleft()
    if x == 100:  # 100번 칸에 도착
        print(cnt[x])
        break
    for i in range(1, 7):  # 주사위 1~6까지 굴림
        next = x + i
        if next <= 100:  # 범위 안에서
            if next in ladders.keys():  # 사다리탈 수 있으면
                next = ladders[next]  # 이동
            elif next in snakes.keys():  # 뱀탈 수 있으면
                next = snakes[next]  # 이동
            if not visited[next]:  # 미방문한 정점이면
                visited[next] = True
                cnt[next] = cnt[x] + 1  # 하나 추가
                q.append(next)
