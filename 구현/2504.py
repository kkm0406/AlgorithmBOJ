# 괄호의 값 S1
# 초기 값을 1로 두고 '(' 괄호가 열릴 때 2를 곱하고,
# '[' 괄호가 열릴 땐 3을 곱하고, 닫을 땐 다시 나누기 2, 3을 해주는 방식이다.
# () [] 처럼 [ 인덱스 바로 뒤 인덱스를 확인하여 ] 괄호가 오는,
# 즉 여는 괄호 바로 뒤가 닫친 괄호인 경우에만 결과 값에다가 덧셈을 한다.
import sys

input = sys.stdin.readline
s = input().strip()
stack = []
ans = 0
tmp = 1  # 괄호값을 계산할 임시 변수
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        tmp *= 2  # 여는 괄호 -> *2
    elif s[i] == '[':
        stack.append(s[i])
        tmp *= 3  # 여는 괄호 -> *3
    elif s[i] == ')':
        if not stack or stack[-1] == '[':  # 올바른 괄호열x
            ans = 0
            break
        if s[i - 1] == '(':  # 이전 값이 (이면
            ans += tmp  # 결과값 갱신
        stack.pop()
        tmp //= 2  # 계산값//2
    elif s[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if s[i - 1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)
