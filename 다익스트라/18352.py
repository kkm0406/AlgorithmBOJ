# 특정 거리의 도시 찾기 S2

import sys
import heapq

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append([b, 1])


def dijkstra(start):
    # 최단거리 리스트
    distance = [sys.maxsize] * (n + 1)
    q = []
    # 시작점에서부터 시작
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 꺼낸 노드에 해당하는 최단 거리 리스트의 값이 더 작은 경우 -> 이미 방문한 노드
        if distance[now] < dist:
            continue

        # 인접한 노드들의 최단거리 갱신
        for v, w in arr[now]:
            # 꺼낸 노드를 거쳐 이동하는 경우
            cost = dist + w
            # 거쳐 이동했을 때 거리가 최단거리보다 작으면
            if cost < distance[v]:
                distance[v] = cost
                # 해당 노드 방문
                heapq.heappush(q, (cost, v))

    return distance


result = dijkstra(x)

ans = []
for i in range(1, n + 1):
    if result[i] == k:
        ans.append(i)

if not ans:
    print(-1)
else:
    for i in ans:
        print(i)
