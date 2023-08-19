# 민준이와 마산 그리고 건우 G4

import sys
import heapq

input = sys.stdin.readline
inf = sys.maxsize
v, e, p = map(int, input().split())
arr = [[] for i in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])


# 다익스트라 알고리즘
def dijkstra(start):
    # 최단거리 리스트
    distance = [inf for i in range(v + 1)]
    distance[start] = 0
    q = []
    # 시작점에서부터 시작
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        # 꺼낸 노드에 해당하는 최단 거리 리스트의 값이 더 작은 경우 -> 이미 방문한 노드
        if distance[now] < dist:
            continue

        # 인접한 노드들의 최단거리 갱신
        for node in arr[now]:
            # 꺼낸 노드를 거쳐 이동하는 경우
            cost = dist + node[1]
            # 거쳐 이동했을 때 거리가 최단거리보다 작으면
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                # 해당 노드 방문
                heapq.heappush(q, (cost, node[0]))
    return distance


# 1번 노드의 최단거리
orgin = dijkstra(1)
# p번 노드의 최단거리
kunwoo = dijkstra(p)

# 건우를 구하지 않았을 때
orgin_path = orgin[-1]
# 건우를 구했을 때
k_path = orgin[p] + kunwoo[-1]

if orgin_path >= k_path:
    print("SAVE HIM")
else:
    print("GOOD BYE")
