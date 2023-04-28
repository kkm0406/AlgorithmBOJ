# 특정한 최단 경로 G4
import sys
import heapq

input = sys.stdin.readline
inf = sys.maxsize
n, e = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, input().split())


# 다익스트라 알고리즘
def dijkstra(start):
    distance = [inf] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    return distance


dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)
dist_1 = dijkstra(1)

# 1->v1->v2->n의 경우와 1->v2->v1->n의 경우중 최소값
result = min(dist_1[v1] + dist_v1[v2] + dist_v2[n], dist_1[v2] + dist_v2[v1] + dist_v1[n])
print(result) if result < inf else print(-1)
