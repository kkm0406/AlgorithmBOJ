# 알바생 강호 S4
import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(n)]
arr.sort(reverse=True)

result = 0
# 주려고 했던 돈이 큰 사람이 앞으로 가게 정렬해야 최댓값
for i in range(n):
    money = arr[i] - i
    if money > 0:
        result += money

print(result)
