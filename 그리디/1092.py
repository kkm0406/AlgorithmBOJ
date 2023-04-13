# 배 G5
import sys

input = sys.stdin.readline
n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
time = 0
crane.sort(reverse=True)  # 내림차순 정렬
box.sort(reverse=True)  # 내림차순 정렬

if crane[0] < box[0]:  # max(크레인) < max(box)
    print(-1)
    sys.exit(0)

while box:
    for i in crane:
        for j in box:
            if i >= j:  # 크레인이 박스를 드는 경우
                box.remove(j)  # 해당 박스 제거
                break
    time += 1

print(time)
