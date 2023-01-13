# 가장 긴 감소하는 부분 수열 S2
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
lis = [1] * n  # 가장 긴 부분 수열의 길이

for i in range(n):
    for j in range(i):  # 이전 원소들과 비교
        if arr[j] > arr[i]:  # 현재 원소값보다 이전 원소가 크면
            lis[i] = max(lis[i], lis[j] + 1)  # 부분 수열 길이+1과 비교

print(max(lis))
