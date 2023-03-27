# 숨바꼭질 3 G5
import heapq
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
distance = [1e9] * 100001


# 이동의 가중치가 다르므로 다익스트라 알고리즘 사용
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        for node in (now + 1, now - 1, now * 2):
            if 0 <= node <= 100000:
                # distance가 1e9인 경우는 아직 방문하지 않은 정점
                if node == now * 2 and distance[node] == 1e9:
                    distance[node] = dist
                    heapq.heappush(q, [dist, node])
                elif distance[node] == 1e9:
                    distance[node] = dist + 1
                    heapq.heappush(q, [dist + 1, node])


dijkstra(n)
print(distance[k])

# ------------------------------------------------
# 순간이동시 걸리는 초가 다르므로 큐를 2개로 나누어 구현
# -> deque를 활용하여 양방향으로 append
dist = [0] * 100001
visited = [False] * 100001
q = deque()
q.append(n)
visited[n] = True
while q:
    now = q.popleft()
    if now == k:
        print(dist[now])
    for move in (now + 1, now - 1, now * 2):
        if 0 <= move <= 100000 and not visited[move]:
            visited[move] = True
            if move == now * 2:
                dist[move] = dist[now]
                q.appendleft(move)  # 순간이동하는 경우는 appendleft
            else:
                dist[move] = dist[now] + 1
                q.append(move)  # 걷는 경우는 append
