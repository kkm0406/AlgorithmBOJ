# 선수과목 G5
# 위상정렬: 사이클이 없는 방향 그래프에서 탐색 순서 파악 시 사용
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
res = [0] * (n + 1)

# 해당 노드로 들어오는 간선 개수를 카운트

prev = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    prev[b] += 1

# 값이 0이면 선수 과목이 없는 것
# 해당 노드를 큐에 삽입
q = deque()
for i in range(1, n + 1):
    if prev[i] == 0:
        q.append([i, 1])

while q:
    now, cnt = q.popleft()
    res[now] = cnt
    # 연결된 간선을 탐색
    for i in arr[now]:
        # 간선과 연결된 노드의 pre - 1
        prev[i] -= 1
        # prev가 0이면 선수과목을 다 들었다는 것 -> 큐에 삽입
        if prev[i] == 0:
            q.append([i, cnt + 1])

print(*res[1:])
