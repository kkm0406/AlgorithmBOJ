# 돌 게임 2 S4
# n이 짝수이면 마지막 돌을 창영이가 가지게 됨 -> 상근이가 이김
# n이 홀수이면 마지막 돌을 상근이가 가지게 됨 -> 창영이가 이김
import sys

n = int(sys.stdin.readline())
if n % 2 == 0:
    print('SK')
else:
    print('CY')
