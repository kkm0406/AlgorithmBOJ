# 트리 G5
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
tree = list(map(int, input().split()))
num = int(input())


def dfs(num):
    tree[num] = -2  # 방문한 노드 처리
    for i in range(n):  # 전체 리스트에서
        if num == tree[i]:  # 방문한 노드를 부모로 하면
            dfs(i)  # 재귀적 dfs로 방문


dfs(num)  # 삭제할 노드부터 dfs로 자식 탐색
cnt = 0
for i in range(n):
    # tree[i] != -2면 삭제된 노드,
    # i가 tree에 있으면 i의 자식 존재 -> 리프노드 아님
    # 따라서 삭제되지 않는 노드 중 자식이 없는 노드
    if tree[i] != -2 and i not in tree:
        cnt += 1
print(cnt)
