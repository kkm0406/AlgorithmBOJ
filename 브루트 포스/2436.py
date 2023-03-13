# 공약수 G5
import math
import sys

input = sys.stdin.readline
n1, n2 = map(int, input().split())

# n1 = 최대공약수, n2 = 최소공배수일 때,
# A = a*n1, B = b*n1라 할 수 있다
# -> 최소공배수는 최대공약수*서로소 a*서로소 b
div = n2 // n1  # a*b = n2/n1
min_sum = 200000000
ans = [0, 0]


# 유클리드 호제법 사용
def gcd(i, j):
    if i % j == 0:
        return j  # 최대 공약수
    return gcd(j, i % j)


# 1부터 div의 제곱근까지
for i in range(1, int(math.sqrt(div)) + 1):
    j = div // i
    if div % i == 0 and gcd(i, j) == 1:  # i가 약수고 i, j가 서로소이면
        if j - i < min_sum:  # 두 수의 차가 최소일 때
            min_sum = j - i
            ans = [i * n1, j * n1]

print(*ans)
