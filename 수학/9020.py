# 골드바흐의 추측 S2

import sys

input = sys.stdin.readline
# 에라스토테네스의 체로 소수를 먼저 구함
prime = [False, False] + [True] * 10000
for i in range(2, 10001):
    if prime[i]:
        for j in range(i * 2, 10001, i):
            prime[j] = False

for _ in range(int(input())):
    n = int(input())
    # 입력한 수의 절반으로 a, b를 설정
    # ex) 8인 경우 a, b = 4, 4
    a = b = n // 2
    while a > 0:
        # a, b가 모두 소수이면
        # n이 6인 경우 초기 a, b는 모두 3이므로
        # 두 소수의 차가 가장 작음
        if prime[a] and prime[b]:
            print(a, b)
            break
        # 모두 소수가 아니면 다른 수로 탐색
        else:
            a -= 1
            b += 1
