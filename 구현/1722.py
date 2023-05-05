# 순열의 순서 G5
import sys
import math

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
nums = [i for i in range(1, n + 1)]

if arr[0] == 1:
    # K = 35이면 25~48이므로 앞자리가 2라는 것을 알 수 있다.
    # 다음 스텝으로 넘어가면 n = 4, k = 35 - 24 = 11이다.
    # 즉, 맨 2 이전의 숫자인 1이 맨 앞자리에 오는 경우는 24가지를 전부 지나치고 2가 맨 앞일 때 11번째 숫자를 찾는 경우이다.
    # 다시 말해서 N = 4, K = 11 일 때로 넘어오게 된다.
    # 이 과정을 재귀로 구현하여 값들을 뽑아보면 다음과 같이 나오게 된다.
    k = arr[1]
    result = []
    for i in range(n, 0, -1):
        fac = math.factorial(i - 1)  # i-1개의 숫자일 때 경우의 수
        step = (k - 1) // fac  # 이전의 fac가지를 지나침
        result.append(nums[step])  # num[step]이 들어옴
        del nums[step]  # 해당 숫자 제거
        k -= fac * step  # fac*step가지 지나감
    print(*result)
else:
    # 순열이 주어지면 그게 몇 번째 순열인지 알아내야 한다.
    # N = 5, K = 2, 3, 5, 1, 4 일 때
    # N = 5, 5! = 120, 120 / N = 24이다.
    # 맨 앞자리가 2이므로 25 ~ 48 에 포함되어 있다. +24
    # 그 다음 3이므로 다음 7 ~ 12 에 포함되어 있다. +6
    # 그 다음 5이므로 다음 5 ~ 6 에 포함되어 있다. +4
    # 그 다음 1이므로 다음 1 ~ 1 에 포함되어 있따. + 1
    # 마지막 4는 자동으로 결정 되므로 위의 숫자들을 더하면 35가 나오게 된다!
    arr = arr[1:]
    k = 1
    for i in range(n, 0, -1):
        fac = math.factorial(i - 1)  # i-1개의 숫자일 때 가능한 개수
        step = nums.index(arr[n - i])  # arr의 n-i번째 숫자가 맨 앞으로 오게 됨
        del nums[step]  # 해당 숫자 삭제
        k += fac * step  # i-1개의 숫자에서 step이 앞자리일 때 가능한 범위 = fac*step
    print(k)
