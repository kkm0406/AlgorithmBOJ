# 수강신청 S3

import sys

input = sys.stdin.readline
k, l = map(int, input().split())
std = {}
for i in range(l):
    id = input().rstrip()
    if not std:  # 대기목록이 빈 경우
        std[id] = i  # 추가
    else:
        if id in std:  # 이미 대기열에 들어간 상태에서 누른경우
            del std[id]  # 삭제하고
            std[id] = i  # 맨뒤로 밀려남
        else:
            std[id] = i

if k > len(std):  # k가 대기목록보다 클 경우
    k = len(std)

arr = list(std.keys())
for i in range(k):
    print(arr[i])
