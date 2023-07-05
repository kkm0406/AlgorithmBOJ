# 도시 분할 계획 G4

import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i


# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 간선에 대한 정보를 담고 있는 그래프 리스트를 비용순으로 정렬
arr.sort(key=lambda x: x[2])
result = 0
max_cost = 0

for node in arr:
    start, end, cost = node
    # 간선을 확인하면서 사이클이 생기는지 확인
    # 사이클이 안생기면 집합에 포함하고 비요ㅗㅇ 업데이트
    if find_parent(start) != find_parent(end):
        union(start, end)
        result += cost
        # 최소 스패닝 트리가 완성되면 비용이 가장 큰 간선을 지워야함
        max_cost = max(max_cost, cost)

print(result - max_cost)
