# 강의실 배정 G5
import heapq
import sys

input = sys.stdin.readline
n = int(input())
# 시작시간 기준 정렬
arr = sorted([list(map(int, input().split())) for _ in range(n)])

# 종료시간이 빠른 강의부터 다음 수업을 이어야하기에 우선순위큐를 사용해 정렬상태 유지
room = []
heapq.heappush(room, arr[0][1])  # 첫회의의 종료시간을 큐에 추가

# 다음 수업의 시작시간에 현재 수업의 종료시간보다 빠르면 새로운 강의실 필요, 아니면 기존 강의실 사용
for i in range(1, n):
    if arr[i][0] < room[0]:  # arr의 i번째 시작시간이 현재 강의가 끝나는 시간보다 빠르면
        heapq.heappush(room, arr[i][1])  # 새로운 강의실 필요
    else:  # 현재 강의실에 이어서 수업가능
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])

print(len(room))
