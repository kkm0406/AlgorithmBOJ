# 트리 나라 관광 가이드 S1
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
tree = set()  # 순서를 보장하지 않아도 되는 경우 list 대신 set을 이용해 시간 단축
parent = [-1] * 200001

parent[arr[0]] = -1
tree.add(arr[0])
for i in range(1, n):
    # 한번도 방문하지 않은 노드는 (해당 노드가 등장하기 전 노드)의 자식
    if arr[i] not in tree:  # 세트에서의 x in s 연산의 평균 시간 복잡도 : O(1)
        parent[arr[i]] = arr[i - 1]
        tree.add(arr[i])  # 트리에 추가

print(len(tree))
for i in range(len(tree)):
    print(parent[i], end=" ")
