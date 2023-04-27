# 신기한 소수 G5
import sys

input = sys.stdin.readline
n = int(input())
primes = [2, 3, 5, 7]  # 첫째자리에 소수가 와야함


# 소수 판별
def is_prime(num):
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return 0
    else:
        return 1


def dfs(depth, num):
    if depth == n:
        print(num)
    else:
        # 짝수면 소수가 아니니까 1~9중 소수만 확인
        for i in range(1, 10, 2):
            # 새로운 수가 소수면
            if is_prime(num * 10 + i) == 1:
                # 재귀적 진행
                dfs(depth + 1, num * 10 + i)
            else:
                continue


# 첫째자리 소수 고정
for i in primes:
    dfs(1, i)
