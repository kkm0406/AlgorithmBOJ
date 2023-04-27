# 도서관 G5
# 음수와 양수를 나누고, 절대값이 큰 수부터 m개씩 분류
# 각 묶음에서 절대값이 가장 큰 수만큼만 움직이면 됨
# 움직여야 하는 값이 가장 큰 묶음을 돌아오지 않음
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dist, plus, minus = [], [], []

for i in arr:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)

# 양수는 내림차순, 음수는 오름차순 졍럴
plus.sort(reverse=True)
minus.sort()

# m권을 들고 음수 좌표의 책을 두는 거리의 절대값 저장
# m*i번째 리스트를 dist에 추가
for i in range(len(minus) // m):
    dist.append(abs(minus[m * i]))
# if문을 통해 남는 리스트 중 가장 큰 값을 dist에 저장
if len(minus) % m > 0:
    dist.append(abs(minus[(len(minus) // m) * m]))

for i in range(len(plus) // m):
    dist.append(plus[m * i])
if len(plus) % m > 0:
    dist.append(plus[(len(plus) // m) * m])

dist.sort()
result = dist.pop()
result += sum(dist) * 2
print(result)
