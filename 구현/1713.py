# 후보 추천하기 S1
import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
arr = list(map(int, input().split()))

std = {}
for i in range(k):
    if arr[i] in std:
        std[arr[i]][0] += 1  # 기존에 있는 학생이면 +1
    else:
        if len(std) < n:
            std[arr[i]] = [1, i]  # 사진틀에 게시가능하면 추가
        else:  # 사진틀이 차있으면
            del_list = sorted(std.items(), key=lambda x: x[1])  # 오래된순 정렬
            std.pop(del_list[0][0])  # 첫번째 학생 제거
            std[arr[i]] = [1, i]  # 새로운 학생 추가

std = sorted(std.keys())

for i in std:
    print(i, end=" ")
