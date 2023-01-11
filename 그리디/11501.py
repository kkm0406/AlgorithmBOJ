# 주식 S2
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split()))
    profit = 0  # 최대 가격
    result = 0  # 최종 이익
    for i in range(n - 1, -1, -1):  # 뒤에서부터 접근하여 
        if profit < stock[i]:  # 최대 가격보다 오늘 가격이 높으면
            profit = stock[i]
        else:  # 현재 수익에 주식 가격을 빼면 이익
            result += profit - stock[i]
    print(result)
