# 나무 자르기 S2

import sys

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

# 성장속도가 가장 빠른 나무를 가장 마지막에 잘라야함
# 성장속도가 더딘 순으로 정렬 후 연산
tree = [[h[i], a[i]] for i in range(n)]
tree.sort(key=lambda x: x[1])
result = 0
for i in range(n):
    result += tree[i][0] + tree[i][1] * i
print(result)
