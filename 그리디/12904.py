# A와 B G5
import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

# 1. 문자열의 뒤에 A를 추가한다.
# 2. 문자열을 뒤집고 뒤에 B를 추가한다.
# 1, 2번 연산을 반대로 진행
while len(t) > len(s):
    if t[-1] == 'A':  # A제거
        t = t[:-1]
    elif t[-1] == 'B':  # B제거 후 문자열 뒤집기
        t = t[-2::-1]

if t == s:  # 최종 결과에서 t와 s가 같으면
    print(1)
else:
    print(0)
