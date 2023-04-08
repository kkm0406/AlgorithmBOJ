# 소수&팰린드롬 S1
import sys

input = sys.stdin.readline
n = int(input())
a = [False, False] + [True] * 1003005
primes = []

# 에라스토네스의 체로 소수 구하기
for i in range(2, 1003005 + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, 1003005 + 1, i):
            a[j] = False

for i in primes:  # 소수 중에서
    if n > i:
        continue
    num = str(i)
    # 팰린드롬 검사
    if num == num[::-1]:
        print(num)
        break
