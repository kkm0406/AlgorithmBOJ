# 괄호의 값 S1
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
