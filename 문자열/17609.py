# 회문 G5
import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().strip()

    if s == s[::-1]:
        print(0)
    else:
        # 원본 문자열 앞에서부터 제거, 뒤에서부터 제거
        new_s1, new_s2 = list(s), list(s)
        for i in range(int(len(s) / 2)):
            if s[i] != s[-(i + 1)]:  # 원본 문자열 맨 앞, 맨 뒤 원소 비교가 다를 때
                new_s1.pop(i)  # 앞에서부터 제거
                new_s2.pop(-(i + 1))  # 뒤에서부터 제거
                if new_s1 == new_s1[::-1]:  # 팰린드롬 확인시 맞을 때
                    print(1)
                    break
                if new_s2 == new_s2[::-1]:  # 팰린드롬 확인시 맞을 때
                    print(1)
                    break
                print(2)  # 둘다 아님
                break
