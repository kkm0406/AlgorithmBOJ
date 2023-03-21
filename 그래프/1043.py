# 거짓말 G4
# Union-Find 알고리즘을 사용
# 분리 집합 문제 -> 공통 원소를 가지지 않는 집합
# 문제에서 진실을 아는 집합과 진실을 모르는 집합으로 분리 -> 두 집합은 공통원소를 갖지 않음
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:]
party = []
parent = [i for i in range(n + 1)]  # Union-Find를 위한 리스트
for i in truth:
    parent[i] = 0  # 진실을 아는 사람은 0 할당


def find(a):  # 특정 원소가 속한 집합(부모)을 알려주는 연산
    if parent[a] != a:  # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적 호출
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):  # 2개 원소로 이루어진 집합을 하나의 집합으로 합치기
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    people = list(map(int, input().split()))[1:]
    for i in range(len(people) - 1):  # 파티에 참석한 사람들에 대해 2명씩 union 실행
        union(people[i], people[i + 1])
    party.append(people)

cnt = 0
for i in party:
    for j in range(len(i)):
        if find(i[j]) == 0:
            break
    else:
        cnt += 1

print(cnt)
