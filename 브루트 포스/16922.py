# 로마 숫자 만들기 S3

import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
n = int(input())
rome = ["I", "V", "X", "L"]
# 각 문자와 숫자를 딕셔너리로 저장
word = {"I": 1, "V": 5, "X": 10, "L": 50}
# n개의 문자를 사용하는 중복순열 구하기
perms = list(combinations_with_replacement(rome, n))
result = set()

# 각 문자열이 나타내는 값 구하기
for perm in perms:
    sum = 0
    for i in perm:
        sum += word[i]
    result.add(sum)

print(len(result))
