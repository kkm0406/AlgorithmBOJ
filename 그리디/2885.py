# 초콜릿 식사 S2

import sys

input = sys.stdin.readline

k = int(input())
# k보다 크면서 가장 작은 2^n 구하기
size = 1
while k > size:
    size = size * 2
cnt = 0
print(size, end=" ")
# size를 반씩 줄이면서 합을 k로 만들기
result = 0
while True:
    if k % size == 0:
        break
    else:
        size //= 2
        cnt += 1

print(cnt)
