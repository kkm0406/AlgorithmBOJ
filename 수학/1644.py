# 소수의 연속합 G3
import sys

n = int(sys.stdin.readline())


def find_prime(n):
    # 에라스토테네스의 체 활용
    arr = [True] * (n + 1)
    arr[0], arr[1] = False, False
    for i in range(2, n + 1):
        if arr[i]:
            j = 2

            while i * j <= n:
                arr[i * j] = False
                j += 1
    return arr


arr = find_prime(n)
primes = []

for i in range(len(arr)):
    if arr[i]:
        primes.append(i)

cnt = 0
# 투포인터 알고리즘 사용
# 1차원 리스트에서 각자 다른 원소를 가리키고 있는 2개의 포인터를 조작
# start, end를 활용하여 start ~ end까지의 합을 구함
# end는 항상 start를 초과하고 두 포인터 모두 증가
start = 0
end = 1
while end <= len(primes):
    tmp_sum = sum(primes[start:end])
    if tmp_sum == n:
        cnt += 1
        end += 1
    elif tmp_sum < n:
        end += 1
    else:
        start += 1
print(cnt)
