# 입력 예시
# https://lagooni.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-%ED%8A%B8%EB%A6%AC-%EC%88%9C%ED%9A%8C-%EC%A0%84%EC%9C%84-%EC%88%9C%ED%9A%8C-%EC%A4%91%EC%9C%84-%EC%88%9C%ED%9A%8C-%ED%9B%84%EC%9C%84-%EC%88%9C%ED%9A%8C
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


# 전위 순회: 현재 노드 -> 왼쪽 서브트리 -> 오른쪽 서브트리
def preorder(node):
    print(node.data, end=" ")
    if node.left_node is not None:
        preorder(tree[node.left_node])
    if node.right_node is not None:
        preorder(tree[node.right_node])


# 중위 순회: 왼쪽 서브트리 -> 현재 노드 -> 오른쪽 서브트리
def inorder(node):
    if node.left_node is not None:
        inorder(tree[node.left_node])
    print(node.data, end=" ")
    if node.right_node is not None:
        inorder(tree[node.right_node])


# 후위 순회: 왼쪽 서브트리 -> 오른쪽 서브트리 -> 현재 노드
def postorder(node):
    if node.left_node is not None:
        postorder(tree[node.left_node])
    if node.right_node is not None:
        postorder(tree[node.right_node])
    print(node.data, end=" ")


n = int(input())
tree = {}
# tree의 인덱스는 KEY로, 저장되는 값은 VALUE로 dictionary에 저장
# {"A" : ("B","C")}
# 👉 의미 : A가 부모인 노드가 B, C / A의 자식이 B, C
for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == '.':
        left_node = None
    if right_node == '.':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
