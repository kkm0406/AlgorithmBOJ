# 거짓말 G4
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
truth = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & truth:  # & -> 교집합 연산
            truth = truth.union(party)  # union -> 합집합 연산

cnt = 0
for party in parties:
    if party & truth:
        continue
    cnt += 1

print(cnt)
