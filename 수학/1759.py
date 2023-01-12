# 암호만들기 G1
import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
alpha = sorted(list(sys.stdin.readline().split())) #미리 오름차순 정렬
combi = list(combinations(alpha, l)) #조합 사용
vowels = ['a', 'e', 'i', 'o', 'u']

for i in combi:
    cnt1, cnt2 = 0, 0
    for j in i:
        if j in vowels: #해당 조합에 모음개수 확인
            cnt2 += 1
        else:
            cnt1 += 1
    if cnt2 >= 1 and cnt1 >= 2:
        print(''.join(i))
