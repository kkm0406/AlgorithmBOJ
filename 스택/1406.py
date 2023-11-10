# 에디터 S2

import sys

input = sys.stdin.readline

# 스택 두 개를 사용해 풀이
# 커서를 기준으로 문자열으 스택 두개에 나누어 저장
edit = list(input().strip())
edit2 = []  # 방향이 뒤집어져 있다고 생각
for i in range(int(input())):
    command = list(input().split())
    # edit에 문자가 있으면 마지막 원소를 edit2에 추가
    if command[0] == 'L':
        if edit:
            edit2.append(edit.pop())
    # edit2의 마지막 원소를 edit로 추가
    elif command[0] == 'D':
        if edit2:
            edit.append(edit2.pop())
    elif command[0] == 'B':
        if edit:
            edit.pop()
    else:
        edit.append(command[1])

# edit2를 reverse해서 더함
answer = edit + edit2[::-1]
print("".join(answer))
