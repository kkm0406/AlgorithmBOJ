# 헨리 G5
import sys
from fractions import Fraction  # 유리수 계산에 사용하는 모듈

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    while a != 1:
        # 1/x <= a / b는
        # x >= b /a로 바꿀 수 있다
        x = b // a + 1
        a = a * x - b
        b = b * x
        # Fraction(a, b) -> a/b형태로 출력
        a, b = map(int, str(Fraction(a, b)).split('/'))
    print(b)
