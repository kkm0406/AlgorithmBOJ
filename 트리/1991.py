# 트리 순회 S1
import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# 전위순회: 방문노드 -> 왼쪽 서브트리 -> 오른쪽 서브트리
def preorder(node):
    print(node.data, end="")
    if node.left is not None:  # 왼쪽 서브트리가 존재하면
        preorder(tree[node.left])  # 재귀적으로 실행
    if node.right is not None:
        preorder(tree[node.right])


# 중위순회: 왼쪽 서브트리 -> 방문 노드 -> 오른쪽 서브트리
def inorder(node):
    if node.left is not None:
        inorder(tree[node.left])
    print(node.data, end="")
    if node.right is not None:
        inorder(tree[node.right])


# 후위 순회: 왼쪽 서브트리 -> 오른쪽 서브트리 -> 방문 노드
def postorder(node):
    if node.left is not None:
        postorder(tree[node.left])
    if node.right is not None:
        postorder(tree[node.right])
    print(node.data, end="")


n = int(input())
tree = {}

for i in range(n):
    data, left, right = input().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[data] = Node(data, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
