# 물병 S1
# N을 이진법으로 바꾸면 (ex, 11 => 1011)
# 물병: 1,1,1,1,1,1,1,1,1,1,1
# 합치기: 2,2,2,2,2,1
# 합치기: 4,4,2,1
# 합치기: 8,2,1
# 결론: N을 이진법으로 바꾼 수의 1의 개수가
# 물을 최대로 합친 후의 물병의 개수이다.
import sys

n, k = map(int, sys.stdin.readline().split())

cnt = 0
while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1')
    cnt += 2 ** idx
    n += 2 ** idx

print(cnt)
