# 카드 정렬하기 G4
import sys
import heapq

input = sys.stdin.readline
n = int(input())
card = []
for i in range(n):
    # 입력한 카드 묶음을 우선순위 큐에 저장 -> 오름차순으로 정렬
    heapq.heappush(card, int(input()))
result = 0

while len(card) > 1:
    # 두묶음씩 pop하여 더함
    sum = heapq.heappop(card)
    sum += heapq.heappop(card)
    # 더한 결과를 다시 우선순위 큐에 저장
    heapq.heappush(card, sum)
    # 더한값 저장
    result += sum

print(result)
