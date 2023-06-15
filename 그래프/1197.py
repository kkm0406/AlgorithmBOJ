# 최소 스패닝 트리 G4
# 최소 스패닝(신장) 트리: 그래프의 최소 연결 부분 그래프
# n개의 정점이 n-1개의 간선으로 연결되어 있으면 트리 형태가 되고 이것이 스패닝트리
# 그 중 가중치 합이 최소인 트리
# 프림 알고리즘 구현
# 시작 정점에서부터 출발해 신장트리 집합을 단계적으로 확장

import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
arr = [[] for i in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])


def prim(start):
    global v
    # 최소 신장 트리에 속했는지 판단하는 리스트
    connected = [False] * (v + 1)
    q = []
    # 그래프에 속하지 않은 연결된 노드들 중 가중치가 작은 순으로 노드를 포함
    # 그래프와 연결된 노드들을 간선의 가중치를 우선순위로 저장하는 우선순위 큐 사용
    # 시작점을 우선순위 큐에 삽입
    heapq.heappush(q, (0, start))
    # 시작 노드일 때 간선 가중치는 0
    weight_sum = 0

    while q:
        # 우선순위큐에 있는 노드들을 pop하면서 그래프에 포함
        w, v = heapq.heappop(q)
        if not connected[v]:  # 최소 신장 트리에 속하지 않았으면
            connected[v] = True  # 포함
            weight_sum += w  # 가중치 더함
            # 노드 v와 연결되어 있으면서 그래프에 포함되지 않은 노드들을 우선순위 큐에 삽입
            for node in arr[v]:
                if not connected[node[0]]:
                    heapq.heappush(q, (node[1], node[0]))

    return weight_sum


result = prim(1)

print(result)
