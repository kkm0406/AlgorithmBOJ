# 파티 G3

import sys
import heapq

inf = sys.maxsize
input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
time = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = node[1] + dist
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


for i in range(1, n + 1):
    distance = [inf] * (n + 1)
    # i번 도시에서 출발
    dijkstra(i, distance)
    # i번 도시에서 x번 도시까지 최단거리 저장
    time[i] = distance[x]

distance1 = [inf] * (n + 1)
# x번 노드에서 출발하는 최단거리
dijkstra(x, distance1)
result = 0
# i번 노드에서 출발하여 x번 도시를 거쳐 되돌아오는 거리 계산
for i in range(1, n + 1):
    time[i] += distance1[i]
    result = max(time[i], result)

print(result)
