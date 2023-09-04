# 외계인의 기타 연주 S1

import sys

input = sys.stdin.readline
n, p = map(int, input().split())

move = 0

# 1 ~ 6번 줄의 스택
st = [[] for i in range(7)]

for _ in range(n):
    l, p = map(int, input().split())
    if not st[l]:  # l번째 스택이 비었으면
        st[l].append(p)  # 추가하고
        move += 1  # 이동 + 1
    else:
        if p > st[l][-1]:  # 스택의 마지막 원소보다 크면
            st[l].append(p)  # 추가하고
            move += 1  # 이동 + 1
        elif p == st[l][-1]:  # 스택 마지막 원소와 같으면 이미 있는 경우
            continue
        else:
            while st[l] and p < st[l][-1]:  # p보다 큰 스택값 삭제
                st[l].pop()
                move += 1
            if st[l] and st[l][-1] == p:  # 스택에 같은 값이 있으면
                continue
            # 스택에 추가하고 이동 + 1
            st[l].append(p)
            move += 1

print(move)
