# 탑 G5
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = []
result = [0] * n

for i in range(n):
    while stack:  # 스택이 있을 때
        if arr[i] > arr[stack[-1]]:  # 현재 탑의 높이가 스택에 있는 탑들의 높이보다 크면
            stack.pop()  # 현재 탑보다 작은 탑의 신호는 못받으므로 스택에서 제거
        else:  # 현재 탑의 높이보다 스택에 있는 탑의 높이가 크면
            result[i] = stack[-1] + 1  # 신호를 받을 수 있으므로 수신받는 탑의 인덱스+1 저장
            break
    stack.append(i)  # 스택에 현재 인덱스 저장
print(*result)
