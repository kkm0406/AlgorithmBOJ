# 최소비용 구하기 2 G3

import sys
import heapq

inf = sys.maxsize
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [[] for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
s, e = map(int, input().split())
distance = [inf] * (n + 1)

prev_node = [0] * (n + 1)


def dijkstra(s):
    distance[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in arr[now]:
            cost = node[1] + dist
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                # 현재 노드 이전에 방문한 노드를 저장
                prev_node[node[0]] = now
                heapq.heappush(q, (cost, node[0]))


dijkstra(s)
result = [e]
path = e  # 도착점에서부터 이전 노드를 거슬러 올라감
while path != s:  # 시작점일 때까지
    path = prev_node[path]  # 현재 노드 직전의 노드
    result.append(path)  # 경로에 저장
result.reverse()  # 역순으로

print(distance[e])
print(len(result))
print(' '.join(map(str, result)))
