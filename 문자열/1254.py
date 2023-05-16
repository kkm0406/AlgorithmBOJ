# 팰린드롬 만들기 S2
import sys

input = sys.stdin.readline
s = list(input().rstrip())

if s == s[::-1]:  # 팰린드롬인 경우
    print(len(s))
else:  # 팰린드롬이 아닌경우
    result = ""  # 팰린드롬을 만들기위해 추가할 문자
    for i in range(len(s)):
        tmp = s[i:]  # 원본 문자열의 i번째부터 슬라이싱
        if tmp == tmp[::-1]:  # 해당 문자열이 팰린드롬이면
            print(len(result) + len(s))
            exit(0)
        else:
            result += s[i]  # 팰린드롬을 만들기위해 i번째 문자를 추가
