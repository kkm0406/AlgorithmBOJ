# 소수 부분 문자열 S1

import sys

input = sys.stdin.readline
visited = [False, False] + [True] * 100000
primes = []

# 에라스토테네스의 체로 소수 구하기
for i in range(2, 100001):
    if visited[i]:
        primes.append(str(i))
        for j in range(2 * i, 100001, i):
            visited[j] = False
while True:
    n = input().rstrip()
    if n == "0":
        break
    num = 0
    for i in range(len(n)):
        tmp = ""
        for j in range(i, len(n)):
            tmp += n[j]  # 앞에서부터 부분 문자열
            if tmp in primes:  # 부분 문자열이 소수이면
                num = max(num, int(tmp))  # 최대값 구하기

    print(num)
