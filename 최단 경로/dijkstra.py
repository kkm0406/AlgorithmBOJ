# 다익스트라 알고리즘
# 1. 출발 노드를 성정
# 2. 최단 거리 테이블을 초기화
# 3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 5. 3번, 4번 반복
# -> 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택하는 그리디 알고리즘
# -> 한 번 처리된 노드의 최단 거리를 고정
import sys

input = sys.stdin.readline
inf = int(1e9)  # 초기 최단거리를 무한으로 설정

n, m = map(int, input().split())  # 노드의 개수, 간선의 개수 입력
start = int(input())  # 시작 노드 번호
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)  # 방문여부 체크 리스트
dist = [inf] * (n + 1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])  # a에서 b로 가는 비용이 c


# 방문하지 않는 노드 중에서, 최단거리가 가장 짧은 노드의 번호 리턴
def get_smallest_node():
    min_val = inf
    idx = 0  # 최단거리가 가장 짧은 노드
    for i in range(1, n + 1):
        if dist[i] < min_val and not visited[i]:
            min_val = dist[i]
            idx = i
    return idx


def dijkstra(start):
    dist[start] = 0  # 출발노드에 대해 초기화
    visited[start] = True  # 방문 처리
    for node in graph[start]:  # 출발노드로부터 이동가능한 노드들의 최단거리 갱신
        dist[node[0]] = node[1]

    # 출발노드 제외 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내, 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for node in graph[now]:
            cost = dist[now] + node[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 최단거리 갱신
            if cost < dist[node[0]]:
                dist[node[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if dist[i] == inf:
        print('INF')
    else:
        print(dist[i])
