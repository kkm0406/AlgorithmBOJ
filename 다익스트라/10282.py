# 해킹 G4

import sys
import heapq

inf = sys.maxsize
input = sys.stdin.readline


def dijkstra(start):
    distance = [inf] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in arr[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

    return distance


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    arr = [[] for i in range(n + 1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        # b 감염 시 a도 감염되므로 b -> a 단방향 연결
        arr[b].append([a, s])
    # c를 시작점으로 다익스트라 진행
    dist = dijkstra(c)
    computer = 0  # 감염된 컴퓨터 수
    time = 0  # 마지막 감염 시간
    for i in range(1, n + 1):
        if dist[i] < inf:
            computer += 1
            # 가장 늦게 감염되는 컴퓨터 찾아서 dist를 감염 시간으로
            if dist[i] > time:
                time = dist[i]

    print(computer, time)
