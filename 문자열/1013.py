# Contact G5
# 정규표현식 이용
# 어떠한 문자가 특정한 패턴으로 시작하는지 판단하려면 re의 match를 이용
# fullmatch는 문자열 전체가 해당 패턴인지를 검사
import sys
import re

input = sys.stdin.readline
p = re.compile('(100+1+|01)+')
for _ in range(int(input())):
    s = input().strip()
    m = p.fullmatch(s)  # fullmatch로 문자열 전체가 해당 패턴인지를 검사
    if m is None:
        print('NO')
    else:
        print('YES')
