# 회장뽑기 G5

import sys

inf = sys.maxsize
input = sys.stdin.readline
n = int(input())
# 친구가 되는 가중치를 저장할 리스트
dist = [[inf] * (n + 1) for i in range(n + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    # 친구 사이의 가중치를 1로 설정
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:  # 자기 자신의 가중치는 0
                dist[i][j] = 0
            else:
                cost = dist[i][k] + dist[k][j]
                # 다른 친구를 거쳐 친구가 되는 경우
                if dist[i][j] > cost:
                    dist[i][j] = cost
# 회원별 점수를 저장할 딕셔너리
result = {}
for i in range(1, n + 1):
    flag = True
    for j in range(1, n + 1):
        if i == j:
            continue
        # 친구가 아닌 경우가 있을 때
        if dist[i][j] == inf:
            flag = False
            break
    if not flag:
        result[i] = -1
    # 모두와 친구 사이, 친구의 친구사이, 친구의 친구의 친구사이, ...
    else:
        # 회원의 가중치의 최댓값이 회원의 점수
        result[i] = max(dist[i][1:])

# 회원별 점수 중 최솟값
min_val = sorted(result.values())[0]
ans = []
# 최솟값과 같은 점수인 회원 찾기
for i in result.items():
    if i[1] == min_val:
        ans.append(i[0])

print(min_val, len(ans))
print(*sorted(ans))
