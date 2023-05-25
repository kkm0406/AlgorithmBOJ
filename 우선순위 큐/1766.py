# 문제집 G2
# 어떤 문제를 풀 때 그 문제의 선수문제가 있는 경우
# 선수문제를 반드시 먼저 풀어야 하기 때문에 위상정렬 사용
# 1. 진입차수가 0인 정점을 큐에 삽입
# 2. 큐에서 원소를 꺼내 해당 원소와 연결된 간선을 모두 제거
# 3. 제거한 후에 진입차수가 0인 정점을 큐에 삽입
# 4. 2~3의 과정 반복
import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)  # 진입차수를 저장할 리스트
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    indegree[b] += 1  # 진입차수 결정


def topology_sort():
    result = []
    q = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            # 진입차수가 0인 문제들을 넣어줌
            # 앞 번호부터 풀어야하므로 우선순위 큐 사용
            heapq.heappush(q, i)

    while q:
        # 차수가 가장 낮고 문제 번호도 가장 낮은 문제
        now = heapq.heappop(q)
        result.append(now)
        # now가 가리키고 있는 문제들 중
        for node in arr[now]:
            # 해당 문제를 풀었으니 진입차수 -1
            indegree[node] -= 1
            # 해당 문제의 진입차수가 0이 되면 풀 수 있으므로 우선순위 큐에 push
            if indegree[node] == 0:
                heapq.heappush(q, node)

    print(*result)


topology_sort()
