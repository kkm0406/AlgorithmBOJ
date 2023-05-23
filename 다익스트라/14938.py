# 서강그라운드 G4

import sys
import heapq

input = sys.stdin.readline
inf = sys.maxsize
n, m, r = map(int, input().split())
# 1~n의 지점이므로 인덱스 맞추기 위해 0추가
t = [0] + list(map(int, input().split()))
arr = [[] for i in range(n + 1)]
for i in range(r):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
result = 0


def dijkstra(start):
    global result
    # 최단거리 리스트
    distance = [inf] * (n + 1)
    distance[start] = 0
    q = []
    # 시작점에서부터 시작
    heapq.heappush(q, (0, start))

    while q:
        # 최단 거리가 가장 짧은 노드
        dist, now = heapq.heappop(q)
        # 꺼낸 노드의 거리값이 최단거리 리스트의 값보다 크면 이미 방문한 정점
        if distance[now] < dist:
            continue

        # 인접한 노드의 최단거리 갱신
        for node in arr[now]:
            cost = node[1] + dist
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

    sum = 0
    # 수색범위 내 아이템 개수
    for i in range(1, len(distance)):
        if distance[i] <= m:
            sum += t[i]
    result = max(result, sum)


# 각 지점에서 다익스트라 진행
for i in range(1, n + 1):
    dijkstra(i)

print(result)
