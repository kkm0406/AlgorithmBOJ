# 좋은 수열 G4

import sys

input = sys.stdin.readline
n = int(input())
result = []


def check(result, depth):
    for k in range(depth):
        # k번째 문자부터 슬라이싱
        tmp = result[k:]
        for i in range(1, len(tmp) // 2 + 1):
            # tmp의 i번째까지 슬라이싱
            new_tmp = tmp[:i]
            # i ~ i*2번째 문자가 같으면 나쁜 순열
            if new_tmp == tmp[i:i * 2]:
                return False
    return True


def dfs(depth):
    # 나쁜 순열인지 확인
    if not check(result, depth):
        return - 1
    if depth == n:
        print(*result, sep="")
        return 0
    for i in range(1, 4):
        # 1, 2, 3의 숫자를 추가
        result.append(i)
        if dfs(depth + 1) == 0:
            return 0
        # result에서 pop
        result.pop()


dfs(0)
