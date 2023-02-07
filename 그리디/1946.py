# 신입 사원 S1
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])

    arr.sort(key=lambda x: x[0])  # 서류 점수 기준 정렬
    cnt = 1  # 서류 1등은 무조건 합격
    hire = arr[0][1]  # 서류 1등의 면접 점수
    for i in range(1, n):
        if arr[i][1] < hire:  # 가장 최근 합격자보다 면접접수가 높으면
            cnt += 1  # 합격
            hire = arr[i][1]  # 최신화

    print(cnt)
