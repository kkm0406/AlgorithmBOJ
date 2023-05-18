# 양팔저울 S1

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
result = set()


# 재귀적으로 주어진 추를 더하거나, 빼서 만들어지는 경우 탐색
def dfs(depth, num):
    result.add(num)
    # 모든 추를 사용했을 때
    if depth >= n:
        return
    dfs(depth + 1, num)
    dfs(depth + 1, num + arr[depth])  # 주어진 추를 더할 때
    dfs(depth + 1, abs(num - arr[depth]))  # 주어진 추를 뺄 때


dfs(0, 0)

# (1부터 S까지의 경우) - (만들어지는 수 - 1)
# 처음 dfs할 때 0이 들어감
print(sum(arr) - (len(result) - 1))
