# 피보나치 S1
import sys

input = sys.stdin.readline
fibo = [0, 1, 1, 2]

# 최대 1000000000까지의 피보나치 수열
while fibo[-1] <= 1000000000:
    fibo.append(fibo[-1] + fibo[-2])

for _ in range(int(input())):
    n = int(input())
    arr = []  # 피보나치 수 저장
    idx = 0
    # n보다 작은 피보나치 수의 인덱스
    while fibo[idx] <= n:
        idx += 1
    idx -= 1
    # n 보다 작은 피보나치 수 추가
    arr.append(fibo[idx])
    n -= fibo[idx]  # 추가한만큼 빼기
    for i in range(idx, -1, -1):  # 뒤에서부터 앞으로 가면서
        if fibo[i] <= n:  # 현재 n보다 피보나치 수가 작으면
            arr.append(fibo[i])  # 리스트 추가
            n -= fibo[i]  # 추가한만큼 빼기

    if n != 0:  # 연산후 n이 0이 아니면
        # 그만큼 1추가
        while n >= 0:
            arr.append(1)
            n -= 1

    for i in range(len(arr) - 2, -1, -1):
        print(arr[i], end=" ")
    print()
