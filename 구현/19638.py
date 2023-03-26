# 센티와 마법의 뽕망치 S1
import heapq
import math
import sys

input = sys.stdin.readline
n, h, t = map(int, input().split())

# 매번 가장 키가 큰 거인 중 하나를 때리기 때문에 우선순위큐를 사용해 정렬상태 유지
arr = []
for i in range(n):
    heapq.heappush(arr, -int(input()))


def check():
    for height in arr:
        if -height >= h:
            return False
    return True


# 처음 거인의 키가 모두 센티보다 작을 경우 확인
flag = check()
if flag:
    print("YES")
    print(0)
    sys.exit(0)

# 뿅망치 횟수만큼 반복
for i in range(1, t + 1):
    height = -heapq.heappop(arr)
    if height == 1:  # 키가 1인 경우 더 줄어들 수 없음
        heapq.heappush(arr, -height)
    else:  # 뿅망치 맞을 경우
        heapq.heappush(arr, -math.floor(height / 2))
    flag = check()  # 거인의 키가 센티보다 작은지 확인
    if flag:
        print("YES")
        print(i)
        sys.exit(0)

# 뿅망치 사용 이후에 센티보다 큰 거인이 있는 경우
if not flag:
    print("NO")
    print(-heapq.heappop(arr))
