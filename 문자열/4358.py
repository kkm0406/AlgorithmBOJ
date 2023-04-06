# 생태학 S2
import sys
from collections import defaultdict

input = sys.stdin.readline

trees = defaultdict(int)  # 딕셔너리 값을 0으로 초기화
cnt = 0

while True:
    tree = input().rstrip()
    if not tree:
        break

    cnt += 1  # 전체 입력 수
    trees[tree] += 1  # 나무 종류의 수

tree_list = list(trees.keys())
tree_list.sort()

for tree in tree_list:
    print("{} {:.4f}".format(tree, trees[tree] / cnt * 100))
