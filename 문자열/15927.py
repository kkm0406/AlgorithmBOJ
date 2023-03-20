# 회문은 회문아니야!! G5
import sys

string = sys.stdin.readline().strip()

if string == string[::-1]:  # 회문인 경우
    s = string[0]
    flag = True
    # 첫번째 문자와 나머지 문자들 비교
    for i in range(1, len(string)):
        if string[i] is not s:  # 첫번째 문자와 다른 문자가 있으면
            flag = False
            break
    if not flag:  # 회문이지만 모든 문자가 같지 않다 -> 마지막 문자만 제거하면 회문이 아님
        print(len(string) - 1)
    else:  # 모든 문자가 같은 경우 -> 항상 회문
        print(-1)
else:  # 회문이 아닌 경우
    print(len(string))
