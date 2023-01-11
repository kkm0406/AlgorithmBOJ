# 안정적인 문자열 S1
import sys

num = 1
while True:
    text = sys.stdin.readline().strip()
    if text.count('-') >= 1:
        break
    text = text.replace("{}", "")
    stack = []
    cnt = 0
    for i in range(len(text)):
        if text[i] == '}':  # 닫는 괄호
            if not stack:  # 스택에 없으면
                cnt += 1
                stack.append('{')
                # {로 바꿔 스택에 저장
            else:  # 스택 마지막 원소가 {이므로 pop
                stack.pop()
        else:  # {만 저장됨
            stack.append(text[i])
    # '{' 개수의 절반만 '}'로 바꾸면 됨
    cnt += len(stack) // 2
    print(f"{num}. {cnt}")
    num += 1
