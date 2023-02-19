# 완전 이진 트리 S1
# 중위순회를 반대로 실행해야 한다.
# level 활용하기
# 중위순회 입력된 리스트 가운데가 항상 root 노드
# 중위 순회로 입력된 리스트를 왼쪽 서브트리, 오른쪽 서브트리로 재귀적으로 나눔.
import sys

input = sys.stdin.readline
k = int(input())
tree = list(map(int, input().split()))
ans = [[] for i in range(k)]


def dfs(arr, depth):
    mid = len(arr) // 2
    ans[depth].append(arr[mid])
    if len(arr) == 1:
        return
    dfs(arr[:mid], depth + 1)
    dfs(arr[mid + 1:], depth + 1)


dfs(tree, 0)
for i in ans:
    print(*i)
