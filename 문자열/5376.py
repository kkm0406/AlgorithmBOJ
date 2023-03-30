# 소수를 분수로 S1
import sys
from math import gcd

input = sys.stdin.readline
for _ in range(int(input())):
    string = input().strip()
    dot = string.find('.')
    if '(' in string:  # 순환소수인 경우 -> https://mathbang.net/238#gsc.tab=0
        start = string.find('(')
        end = string.find(')')
        recur = string[start + 1:end]
        before = string[dot + 1:start]
        n1_left = 10 ** (len(before + recur))
        n2_left = 10 ** (len(before))
        n1_right = before + recur
        n2_right = before
        if n2_right == "":
            n2_right = '0'
        parent = int(int(n1_left) - int(n2_left))
        child = int(int(n1_right) - int(n2_right))
    else:  # 순환소수가 아닌경우
        parent = int((10 ** (len(string[:dot]) - 1)) * (10 ** (len(string[dot + 1:]))))
        child = int(string[:dot] + string[dot + 1:])
    print(f"{child // gcd(parent, child)}/{parent // gcd(parent, child)}")
