# 백도어 G5
import heapq
import sys

INF = sys.maxsize
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr[-1] = 0
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    graph[b].append([a, t])

# 최단거리 리스트
distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    # 출발노드로 가는 최단경로 갱신
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단거리가 가장 짧은 노드 pop
        dist, now = heapq.heappop(q)
        # 꺼낸 노드의 거리값이 최단거리 리스트의 값보다 크다는 것은 이미 방문했다는 것
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 노드 중
        for v, w in graph[now]:
            cost = dist + w
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧음 and 시야에 안걸림
            if cost < distance[v] and arr[v] == 0:
                distance[v] = cost
                heapq.heappush(q, (cost, v))


dijkstra(0)
print(distance[n - 1]) if distance[n - 1] != INF else print(-1)
