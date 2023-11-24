# 랭킹전 대기열 S1
import math
import sys

input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)
    if not rooms:
        # 맨 처음 방 생성
        rooms.append([[l, n]])
    else:
        # 새로운 방 생성 여부
        flag = False
        for i in range(len(rooms)):
            # 방의 정원 미달 그리고 입장 가능한 레벨의 방일 때
            if len(rooms[i]) < m and rooms[i][0][0] - 10 <= l <= rooms[i][0][0] + 10:
                # 해당 방에 입장
                rooms[i].append([l, n])
                # 새로운 방 생성 x
                flag = True
                break
        # 새로운 방 생성
        if not flag:
            rooms.append([[l, n]])

for room in rooms:
    # 이름순 정렬
    room.sort(key=lambda x: (x[1], x[0]))
    # 정원이 찬 방
    if len(room) == m:
        print('Started!')
    # 정원 미달
    else:
        print('Waiting!')
    for l, n in room:
        print(l, n)
