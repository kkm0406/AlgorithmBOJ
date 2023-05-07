# 숫자 할리갈리 게임 S1
# pypy 제출
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
do = deque()
su = deque()
ground_do = []
ground_su = []
for _ in range(n):
    a, b = map(int, input().split())
    do.append(a)
    su.append(b)

for i in range(0, m, 1):
    if i % 2 == 0:  # 도도먼저 카드 뽑음
        do_top = do.pop()
        ground_do.append(do_top)
    else:  # 그다음 수연이 카드 뽑음
        su_top = su.pop()
        ground_su.append(su_top)

    # 덱이 빈 사람이 있으면 상대방 승
    if not do:
        print('su')
        break
    elif not su:
        print('do')
        break

    # 그라운드에서 가장 위에 위치한 카드들 합이 5면 수연이 종침
    if ground_do and ground_su and ground_do[-1] + ground_su[-1] == 5:
        # 도도 그라운드의 카드를 덱 아래에 합침
        for card in ground_do:
            su.appendleft(card)
        ground_do.clear()
        # 수연 그라운드의 카드를 덱 아래에 합침
        for card in ground_su:
            su.appendleft(card)
        ground_su.clear()

    # 그라운드의 가장 위에 위치한 카드들 중 5가 있으면 도도가 종침
    if (ground_do and ground_do[-1] == 5) or (ground_su and ground_su[-1] == 5):
        for card in ground_su:
            do.appendleft(card)
        ground_su.clear()
        for card in ground_do:
            do.appendleft(card)
        ground_do.clear()
else:
    if len(do) == len(su):
        print('dosu')
    elif len(do) > len(su):
        print('do')
    else:
        print('su')
