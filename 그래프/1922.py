# 네트워크 연결 G4
# 스패닝트리(신장트리): 그래프의 최소 연결 부분 그래프
# - 그래프에서 일부 간선을 선택해서 만든 트리
# - n개의 정점을 가지는 그래프의 최소 간선의 수는 n-1개, n-1개의 간선으로 연결
# - 사이클 포함x, 모든 정점이 연결
# 최소스패닝트리: 신장트리 중 사용된 간선들의 가중치 합이 최소인 트리
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = []
parent = [i for i in range(n + 1)]
result = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])


def find(a):
    if parent[a] == a:  # 자신이 루트노드면 자신을 반환
        return a
    parent[a] = find(parent[a])  # 재귀적으로 a의 부모노드를 갱신
    return parent[a]


def union(a, b):  # a, b를 병합
    a = find(a)  # a의 부모 노드 탐색
    b = find(b)  # b의 부모 노드 탐색
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


graph.sort(key=lambda x: x[0])  # 가중치로 정렬
for dist, a, b in graph:
    if find(a) != find(b):  # a, b의 부모노드가 다르면
        union(a, b)  # a, b를 병합
        result += dist  # 비용 갱신
print(result)
