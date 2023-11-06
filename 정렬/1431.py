# 시리얼 번호 S3
import sys

input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    string = input().strip()
    size = len(string)  # 시리얼번호 길이
    sum = 0  # 시리얼번호 합
    for i in string:
        if i.isdigit():  # i가 숫자면
            sum += int(i)  # 더함
    arr.append([string, size, sum])

# 문자열 길이, 합, 사전순으로 정렬
arr.sort(key=lambda x: (x[1], x[2], x[0]))

for i in arr:
    print(i[0])
