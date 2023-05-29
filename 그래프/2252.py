# 줄 세우기 G3
# 위상정렬
# 1. 차수가 0인 정점을 큐에 삽입
# 2. 큐에서 원소를 꺼내 해당 원소와 연결된 간선을 모두 제거
# 3. 제거한 후에 차수가 0인 정점을 큐에 삽입
# 4. 2-3의 과정을 반복

import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)  # 차수를 저장할 리스트
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    indegree[b] += 1  # 차수 갱신


def topology_sort():
    result = []
    q = []

    for i in range(1, n + 1):
        if indegree[i] == 0:  # 차수가 0인 정점을
            heapq.heappush(q, i)  # 우선순위 큐에 삽입

    while q:
        # 차수가 가장 낮은 정점
        now = heapq.heappop(q)
        result.append(now)
        # 연결된 정점 탐색
        for node in arr[now]:
            # 차수를 1씩 줄임
            indegree[node] -= 1
            # 차수가 0이 되면 다시 우선순위 큐에 삽입
            if indegree[node] == 0:
                heapq.heappush(q, node)
    return result


result = topology_sort()
print(*result)
