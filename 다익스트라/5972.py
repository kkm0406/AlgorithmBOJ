# 택배 배송 G5
import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    # 양방향 그래프
    graph[b].append([a, c])
    graph[a].append([b, c])

# 최단거리 리스트
distance = [1e9] * (n + 1)


def dijkstra(start):
    distance[start] = 0
    q = []
    # 출발노드로 가는 최단경로 갱신
    heapq.heappush(q, (0, start))

    while q:
        # 최단 거리가 가장 짧은 노드 pop
        dist, now = heapq.heappop(q)
        # 꺼낸 노드의 거리값이 최단거리 리스트의 값보다 크다는 것은 이미 방문했다는것
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 노드들 중
        for node in graph[now]:
            cost = node[1] + dist
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(1)
print(distance[n])
