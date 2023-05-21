# 아이들과 선물 상자 S2

import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
c = list(map(int, input().split()))
w = list(map(int, input().split()))
q = []

# 가장 높은 숫자를 pop해야함 -> 내림차순 최대힙을 만들기 위해 -1를 곱함
for i in c:
    heapq.heappush(q, -i)

flag = True
for i in w:
    # pop한 값에 다시 -1를 곱함
    x = -1 * heapq.heappop(q)
    if x < i:  # 원하는 선물이 남은 선물보다 클 때 -> 못가져감
        flag = False
        break
    # 선물가져간만큼 빼고 다시 push
    heapq.heappush(q, -(x - i))

print("1") if flag else print("0")
