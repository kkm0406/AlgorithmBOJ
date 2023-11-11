# 한국이 그리울 땐 서버에 접속하지 S3
import sys

input = sys.stdin.readline

n = int(input())
# * 기준 패턴 분리
pattern = input().strip().split("*")

for _ in range(n):
    string = input().strip()
    # 입력한 문자열의 길이가 패턴보다 작으면 일치 x
    if len(string) < len(pattern[0]) + len(pattern[1]):
        print("NE")
    else:
        # 첫번째 패턴과 문자열의 앞쪽 비교, 두번째 패턴과 문자열의 뒷쪽 비교
        if pattern[0] == string[:len(pattern[0])] and pattern[1] == string[-len(pattern[1]):]:
            print("DA")
        else:
            print("NE")
