# 단어 맞추기 S1
import sys

input = sys.stdin.readline
n = int(input())


def next_permutation(string):
    # 1. 끝에서부터 비교해 앞에 것이 더 작은 곳을 i로 지정
    i = len(string) - 2
    while i >= 0 and string[i] >= string[i + 1]:
        i -= 1
    if i == -1:  # 해당 문자열이 이미 내림차순인 경우
        return False

    # 2. 끝에서부터 i번째 원소보다 큰 원소를 찾고 해당 인덱스를 j로 지정
    j = len(string) - 1
    while string[i] >= string[j]:
        j -= 1

    # i, j번째 원소 스왑
    string[i], string[j] = string[j], string[i]
    # i번쨰 뒤에 있는 것들 순서 뒤집기
    result = string[:i + 1] + list(reversed(string[i + 1:]))
    return result


for _ in range(n):
    string = list(input().strip())
    result = next_permutation(string)
    if not result:
        print(''.join(string))
    else:
        print(''.join(result))
