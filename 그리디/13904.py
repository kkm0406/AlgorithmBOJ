# 과제 G3
# 점수로 내림차순 정렬을 하되, 그 과제를 먹으려면 최대한 나중에 수행하는 쪽으로 구현
# 예를 들어, (1, 20), (2, 30), (2, 10), (3, 40), (3, 35) 의 과제 데이터가 있을 때,
# 일단은 제일 점수 높은 (3, 40)을 먹을 생각을 한다. 단, 이 과제를 day = 3 일차에 수행한다고 생각하면서 먹는다.
# 그래야 day = 1, 2 일차에 먹을 수 있는 과제의 수가 많아지기 때문이다.
# 만약에 그 과제를 day = 1 일차에 수행한다 치면 day = 1인 과제는 더 이상 먹을 수 없게 되기 때문이다.
# 그리고 나서는 2번째로 점수가 높은 (3, 35) 를 선택한다.
# 하지만 이미 day = 3 일차에는 수행할 과제를 확보해놨기 때문에 그 전인 day = 2 일차에 이 과제를 수행하기로 한다
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key=lambda x: x[1], reverse=True)
result = 0
visited = [False] * 1001
for d, w in arr:
    i = d
    while i > 0 and visited[i]:
        i -= 1
    if i == 0:
        continue
    else:
        visited[i] = True
        result += w

print(result)
