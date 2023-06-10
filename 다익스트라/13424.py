# 비밀 모임 G4
import sys
import heapq

input = sys.stdin.readline
inf = sys.maxsize


def dijkstra(friend):
    distance = [inf] * (n + 1)
    distance[friend] = 0
    q = []
    heapq.heappush(q, [0, friend])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in arr[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, [cost, node[0]])

    return distance


for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [[] for i in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        arr[a].append([b, c])
        arr[b].append([a, c])
    k = int(input())
    friends = map(int, input().split())
    result = []
    # 친구들의 위치에서 모든 방까지 다익스트라로 최단거리
    for friend in friends:
        # 친구들 위치에서의 최단거리 리턴
        dist = dijkstra(friend)
        result.append(dist)

    dist = []
    for i in range(1, n + 1):
        tmp_dist = 0
        # 친구들이 각 방에 도착하는 최단거리를 합함
        for j in range(k):
            tmp_dist += result[j][i]
        # 방번호와 방에 도착하는 최단거리
        dist.append([i, tmp_dist])
    # 거리순, 방 번호순 정렬
    dist.sort(key=lambda x: (x[1], x[0]))
    print(dist[0][0])
