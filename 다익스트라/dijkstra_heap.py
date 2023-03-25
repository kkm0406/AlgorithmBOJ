# 다익스트라 알고리즘 개선: 우선순위 큐 사용
# 단계마다 방문하지 않는 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 heap 사용
# 기본 원리를 동일하지만, 현재 가장 가까운 노드를 저장하기 위해 heap을 추가적으로  (logN의 속도)
# -> 현재 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용
import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)  # 초기 최단거리를 무한으로 설정

n, m = map(int, input().split())  # 노드의 개수, 간선의 개수 입력
start = int(input())  # 시작 노드 번호
graph = [[] for i in range(n + 1)]
dist = [inf] * (n + 1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])  # a에서 b로 가는 비용이 c


def dijkstra(start):
    q = []
    # 출발노드로 가는 최단 경로는 0, 우선순위 큐에 삽입
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 최단 거리가 가장 짧은 노드의 정보 pop
        cost, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 continue
        if dist[now] < cost:  # 현재 꺼낸 노드의 거리값이 최단거리 테이블에 기록된 것보다 크면
            continue
        # 현재 노드와 연결된 다른 노드들 확인
        for node in graph[now]:
            new_cost = cost + node[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if new_cost < dist[node[0]]:
                dist[node[0]] = new_cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(start)

for i in range(1, n + 1):
    if dist[i] == inf:
        print('INF')
    else:
        print(dist[i])
