# 물통 G5
# 물통에 들어있을 수 있는 모든 경우의 수를 찾아서 첫번째 물통이 비어있을 때 세번째 물통의 양을 구한다.
# 물통이 3개지만 물의 총량이 고정이기 때문에 a,b 두 물통만 체크하면 된다. c는 저절로 정해짐.
# a -> b, a -> c, b -> a, b -> c, c -> a, c -> b 6가지를 모두 탐색한다.
import sys
from collections import deque

input = sys.stdin.readline

a, b, c = map(int, input().split())


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append([x, y])


def bfs():
    while q:
        # x: a 물통의 양, y: b 물통의 양, z: c 물통의 양
        x, y = q.popleft()
        z = c - x - y
        # a 물통이 비어있는 경우 c 물통의 양 저장
        if x == 0:
            ans.append(z)

        # x->y로 옮기는 경우
        w = min(x, b - y)  # x->y로 옮길 물(x전체를 옮기거나, b물통을 꽉 채우거나)
        pour(x - w, y + w)
        # x->z로 옮기는 경우
        w = min(x, c - z)
        pour(x - w, y)
        # y->x
        w = min(y, a - x)
        pour(x + w, y - w)
        # y->z
        w = min(y, c - z)
        pour(x, y - w)
        # z->x
        w = min(z, a - x)
        pour(x + w, y)
        # z->y
        w = min(z, b - y)
        pour(x, y + w)


visited = [[False] * (b + 1) for i in range(a + 1)]
ans = []
q = deque()
q.append([0, 0])
visited[0][0] = True
bfs()
ans.sort()
print(*ans)
