# 최단 경로 G4
import heapq
import sys

input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
graph = [[] for i in range(v + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])  # a에서 b로 가는 비용이 c

distance = [1e9] * (v + 1)  # 최단 거리 리스트 초기화


def dijkstra(start):
    q = []
    # 출발노드까지의 최단 경로는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 가장 짧은 노드 pop
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 최단 거리 리스트의 값이 더 작으면 이미 방문했다는 것
            continue
        # 현재 노드와 연결된 노드확인
        for node in graph[now]:
            cost = node[1] + dist
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧으면 최단 거리 갱신
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(k)
for i in range(1, v + 1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])
