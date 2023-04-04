# 간선 이어가기 2 G5
import heapq
import sys

inf = sys.maxsize
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    # 정점에 가중치가 있는 간선 연결
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
s, t = map(int, input().split())
distance = [inf] * (n + 1)  # 최단거리 리스트


def dijkstra(start):
    q = []
    # 시작노드 우선순위큐 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 최단거리 갱신

    while q:
        # 가장 최단거리가 작은 노드 리턴
        dist, now = heapq.heappop(q)
        # 최단거리 리스트의 값이 노드의 최단거리보다 작으면 이미 처리된 것
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = node[1] + dist
            # 현재 노드를 거쳐 다른 노드로 이동하는 것이 최단거리가 더 짧으면
            if distance[node[0]] > cost:
                # 최단 거리 갱신
                distance[node[0]] = cost
                # 현재 노드 우선순위 큐에 삽입
                heapq.heappush(q, (cost, node[0]))


dijkstra(s)  # 시작점부터 다익스트라 진행
print(distance[t])
