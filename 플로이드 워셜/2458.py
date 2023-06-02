# 키 순서 G4
# pypy 제출
import sys

inf = sys.maxsize

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
dist = [[0] * (n + 1) for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    dist[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 자신보다 작은 경우
            if dist[i][j] == 1 or (dist[i][k] == 1 and dist[k][j] == 1):
                dist[i][j] = 1

cnt = 0
for i in range(1, n + 1):
    height = 0
    for j in range(1, n + 1):
        # 자기보다 작은 사람과 큰 사람의 합
        # 자기가 갈 수 있는 노드는 자기보다 작은 사람
        # 자신에게 오는 경우가 있는 노드는 자기보다 큰 사람
        height += dist[i][j] + dist[j][i]
    if height == n - 1:  # 자기 키 순서를 아는 경우
        cnt += 1

print(cnt)
