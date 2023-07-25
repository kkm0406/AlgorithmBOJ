# 에라토스테네스의 체 S4

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
visited = [False, False] + [True] * (n - 1)
arr = []  # 지워지는 수
for i in range(2, n + 1):
    if visited[i]:
        # 2가 가장 먼저 지워짐
        if i not in arr:
            arr.append(i)
        # i의 배수를 차례대로 지움
        for j in range(2 * i, n + 1, i):
            visited[j] = False
            if j not in arr:
                arr.append(j)

print(arr[k - 1])
