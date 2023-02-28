# 팔 S1
import sys

input = sys.stdin.readline
l, r = input().split()

# l과 r의 길이가 다르면 8이 없는 수 무조건 존재
if len(l) != len(r):
    print(0)
else:
    cnt = 0
    for i in range(len(l)):
        # l의 i번째 숫자와 r의 i번째 숫자가 다르면,
        # i번째 이후 8없는 경우 무조건 존재
        # ex) 1483 ~ 2134 -> 1500, 1501,...
        # ex) 8183 ~ 8200 -> 8190, 8191,...
        if l[i] == r[i]:
            if l[i] == '8':
                cnt += 1
        else:
            break
    print(cnt)
