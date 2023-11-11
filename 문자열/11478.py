# 서로 다른 부분 문자열의 개수 S3

import sys

input = sys.stdin.readline

string = input().strip()

arr = set()

for i in range(1, len(string)+1):
    for j in range(len(string) - i+1):
        arr.add(string[j:j+i])

print(len(arr))