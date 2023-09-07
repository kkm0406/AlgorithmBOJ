# 키로거 S2

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    string = input().strip()
    # 커서 위치 구현위해 left, right 사용
    left, right = [], []
    for item in string:
        if item == '-':
            # left에 값이 있으면 지움
            if left:
                left.pop()
        elif item == '<':  # right로 left의 값을 넘김
            if left:
                right.append(left.pop())
        elif item == '>':  # left로 right의 값을 넘김
            if right:
                left.append(right.pop())
        else:
            # 기본적으로 left에 저장
            left.append(item)
    # right를 뒤집어서 left와 더함
    result = left + list(reversed(right))
    print(''.join(result))
