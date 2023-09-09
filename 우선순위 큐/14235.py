# 크리스마스 선물 S3

import sys
import heapq

input = sys.stdin.readline
q = []

for _ in range(int(input())):
    a = list(map(int, input().split()))
    if a[0] == 0:  # 아이를 만났을 때
        if not q:  # 줄 선물이 없으면
            print(-1)
        else:
            print(-1 * heapq.heappop(q))
    else:
        for i in a[1:]:
            # 가장 가치가 큰 선물을 주기 때문에
            # 최대힙 -> -1을 곱해 저장
            heapq.heappush(q, -i)
