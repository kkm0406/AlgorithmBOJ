# 카드 합체 놀이 S1
import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    card = sorted(card)  # 매 합체 시 카드 오름차순 정렬
    result = card[0] + card[1]  # 0번째+1번째
    card[0], card[1] = result, result

print(sum(card))
