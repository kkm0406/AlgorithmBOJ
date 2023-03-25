# 최소비용 구하기 G5
import heapq
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]
distance = [1e9] * (n + 1)  # 최단 거리 리스트
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])  # a에서 b로 가는 비용이 c

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))  # 출발노드까지의 거리 우선순위 큐 저장

    while q:
        # 최단 거리가 가장 짧은 노드 pop
        dist, now = heapq.heappop(q)
        # now까지의 거리가 최단 거리 리스트의 값보다 크면 이미 방문한 노드이므로 continue
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 노드중
        for node in graph[now]:
            cost = node[1] + dist
            # 현재 노드를 거쳐 이동하는 것이 더 최소비용이면 최단 거리 갱신
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(start)
print(distance[end])
