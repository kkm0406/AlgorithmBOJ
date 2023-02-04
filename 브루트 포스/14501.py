# 퇴사 S3
import sys

input = sys.stdin.readline

n = int(input())
t = []
p = []
result = [0 for i in range(n + 1)]  # 해당 날짜 (index)에서부터 퇴사날까지 받을 수 있는 최대 이익

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n - 1, -1, -1):  # 퇴사일을 넘지 않도록 뒤에서 부터 접근
    day = t[i] + i
    if day > n:  # 상담에 필요한 일수가 퇴사일을 넘어가면
        result[i] = result[i + 1]  # 다음날 값 그대로 가져옴
    else:
        result[i] = max(p[i] + result[day], result[i + 1])  # 오늘 상담을 안 할 경우와 상담을 할 경우 중 max 값

print(result[0])
