# 단축키 지정 S1
import sys

input = sys.stdin.readline
n = int(input())
arr = [input().rstrip() for i in range(n)]
check = {' '}  # 단축키 리스트
result = []  # 단축키 설정 후 배열
for string in arr:
    words = string.split()  # 공백 기준 split
    flag = False  # 단축키 설정 여부
    for i in range(len(words)):  # 단어 하나씩 탐색
        if words[i][0].upper() not in check:  # 0번째 글자가 단축키가 아니면
            check.add(words[i][0].upper())  # 단축키에 추가
            words[i] = '[' + words[i][0] + "]" + words[i][1:]  # 단축키에 괄호
            result.append(" ".join(words))  # result에 추가
            flag = True  # 단축키 설정 완료
            break
    if not flag:  # 단축키 설정된게 없으면
        for i in range(len(string)):  # 전체 문자열에서
            if string[i].upper() not in check:  # i번째 문자가 단축키가 아니면
                check.add(string[i].upper())  # 단축키에 추가
                result.append(string[:i] + '[' + string[i] + ']' + string[i + 1:])  # result에 단축키에 괄호 씌우고 저장
                flag = True  # 단축키 설정 완료
                break
    if not flag:  # 단축키 설정할게 없으면
        result.append(" ".join(words))

for i in result:
    print(i)
