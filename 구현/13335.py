# 트럭 S1
import sys

input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = list(map(int, input().split()))

bridge = [0] * w  # 다리 위
weight, cnt = 0, 0

while bridge:  # 마지막 트럭이 들어오고 나올 때까지
    cnt += 1
    bridge.pop(0)  # 다리 첫번째 트럭 pop
    if truck:  # 올라갈 트럭이 있으면
        if sum(bridge) + truck[0] <= l:
            now = truck.pop(0)
            bridge.append(now)
        else:
            bridge.append(0)  # 올라갈 트럭이 있지만 다리에 못 올라갈 경우
            # 공간 채워줘야 함

print(cnt)
