# 여행 가자 G4
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
# 부모 테이블 상에서 자기 자신을 부모로 설정
parent = [i for i in range(n)]


# 노드의 부모 찾기
def find(i):
    # i 노드가 부모 노드이면 i 반환
    if i == parent[i]:
        return i
    # i 노드를 따라가면서 부모 노드 찾기
    p = find(parent[i])
    # 부모 테이블 갱신
    parent[i] = p
    return parent[i]


# i, j 집합 합치기
def union(i, j):
    i = find(i)  # i 노드의 부모 찾기
    j = find(j)  # j 노드의 부모 찾기
    # 동일 집합이면 연결시에 순환
    if i == j:
        return
    # i의 부모가 j의 부모보다 상위 루트이면
    if i < j:
        # j의 부모를 i의 부모로 변경
        parent[j] = i
    else:
        parent[i] = j


for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            # 그래프의 모든 간선 정보가 주어졌을 때,
            # 유니온 파인드를 이용해 특정 정점부터 특정 정점까지 이어져있는지 손쉽게 확인
            union(i, j)

parent = [-1] + parent
plan = list(map(int, input().split()))
#  여행 계획이 모두 한 분리 집합 내에 속한다면 YES, 아니면 NO를 출력
for i in range(1, m):
    if parent[plan[i]] != parent[plan[0]]:
        print('NO')
        break
else:
    print('YES')
