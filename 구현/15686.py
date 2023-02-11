# 치킨 배달 G5
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
home = []
chicken = []
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append([i, j])  # 가정집 위치
        elif arr[i][j] == 2:
            chicken.append([i, j])  # 치킨집 위치

for comb in combinations(chicken, m):  # 조합을 이용해 m개의 치킨집 위치 구함
    result = 0
    for hx, hy in home:
        dist = 2 * n
        for i in range(m):
            # 가정집에서 가장 가까운 치킨집위치 초기화
            dist = min(dist, abs(hx - comb[i][0]) + abs(hy - comb[i][1]))
        result += dist  # 각 조합에서 치킨거리
    ans.append(result)

print(min(ans))  # 치킨거리의 최솟값 출력
