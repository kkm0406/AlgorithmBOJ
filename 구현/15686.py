# 치킨 배달 G5
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
home = []
chicken = []
visited = [[0] * n for i in range(n)]
combs = []
ans = []
last_visited = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])
            visited.append(False)


def dfs(depth):
    if depth == m:
        result = 0
        for hx, hy in home:  # 모든 집과
            dist = 2 * n
            for idx, (cx, cy) in last_visited:  # 뽑은 치킨집과의 거리 구함
                dist = min(dist, abs(hx - cx) + abs(hy - cy))
            result += dist
        ans.append(result)
        return

    for e, (cx, cy) in enumerate(chicken):  # eumerate로 인덱스, 원소 접근
        if visited[cx][cy] == 0:  # 치킨집 방문안했으면
            if last_visited:  # 시간 단축과 오름차순위해
                if e < last_visited[-1][0]:  # 마지막에 방문한 인덱스가 현재 인덱스보다 작으면 continue
                    continue
            visited[cx][cy] = 1  # 치킨집 방문 처리
            last_visited.append((e, (cx, cy)))
            dfs(depth + 1)
            visited[cx][cy] = 0  # 미방문 처리
            last_visited.pop()


dfs(0)
print(min(ans))
