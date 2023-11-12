# 등수 매기기 S3

import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
# 예상 등수 정렬
arr.sort()

result = 0
for i in range(1, n + 1):
    # 1등부터 예상등수와 비교(같으면 0이 더해지기 때문에 상관없음)
    result += abs(i - arr[i - 1])

print(result)
