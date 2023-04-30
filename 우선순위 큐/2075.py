# N번째 큰 수 S2

import sys
import heapq

input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for i in tmp:
        if len(q) < n:  # 우선순위 큐에 있는 원소 개수가 n개 미만이면
            heapq.heappush(q, i)  # 삽입
        else:  # 원소 개수가 n개면
            if q[0] < i:  # 현재 숫자가 우선순위 큐 최소값보다 크면
                heapq.heappop(q)  # 우선순위 큐 최소값 제거
                heapq.heappush(q, i)  # 현재 숫자 삽입

print(q[0])
