# 최대공약수 S1
import sys

input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
a = 1
for i in arr1:
    a *= i
m = int(input())
arr2 = list(map(int, input().split()))
b = 1
for i in arr2:
    b *= i


# 유클리드 호제법을 사용해 최대 공약수 구하기 or math 라이브러리 사용
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


num = list(str(gcd(a, b)))

if len(num) > 9:  # 최대 공약수가 9자리가 넘어가면
    tmp = num[:-10:-1]  # 뒤에서부터 9자리까지 슬라이싱
    print(''.join(reversed(tmp)))  # reverse하여 출력
else:
    print(''.join(num))
