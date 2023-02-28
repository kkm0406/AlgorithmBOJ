# 0 만들기 G5
import sys
from itertools import product

input = sys.stdin.readline
sets = ['-', '+', ' ']
ans = []
for _ in range(int(input())):
    n = int(input())
    arr = [i for i in range(1, n + 1)]
    datas = list(product(sets, repeat=n - 1))  # 연산자 중복 순열
    num = 1
    result = []
    for data in datas:
        # 수식 리스트 계산
        string = ''
        for i in range(n - 1):
            string += str(arr[i]) + data[i]
        string += str(arr[-1])
        if eval(string.replace(' ', '')) == 0:  # eval 함수로 string 형태의 수식 계산
            result.append(string)
    ans.append(sorted(result))

for i in ans:
    for j in i:
        print(j)
    print()
