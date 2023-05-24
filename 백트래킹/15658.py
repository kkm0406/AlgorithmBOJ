# 연산자 끼워넣기 (2) S2

import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
marks = list(map(int, input().split()))
result = []
max_ans = -1 * sys.maxsize
min_ans = sys.maxsize


def dfs(depth):
    global max_ans, min_ans
    if depth == n - 1:
        tmp = a[0]  # 첫번째 값추가
        # 순서대로 계산
        for i in range(1, len(a)):
            mark = result[i - 1]
            if mark == '+':
                tmp += a[i]
            elif mark == '-':
                tmp -= a[i]
            elif mark == '*':
                tmp *= a[i]
            else:
                # -5//2 = -3이 나와서
                # 먼저 양수로 처리한 다음 계산한 값에 -1을 곱함
                if tmp < 0:
                    rmp = -1 * tmp // a[i]
                    tmp = -1 * rmp
                else:
                    tmp //= a[i]
        max_ans = max(max_ans, tmp)
        min_ans = min(min_ans, tmp)
    else:
        # 연산자 종류만큼
        for i in range(4):
            # 연산자 개수가 0보다 크면
            if marks[i] > 0:
                # 인덱스에 맞게 연산자 추가
                if i == 0:
                    result.append('+')
                elif i == 1:
                    result.append('-')
                elif i == 2:
                    result.append('*')
                elif i == 3:
                    result.append('/')
                # 추가한만큼 개수 빼고
                marks[i] -= 1
                # dfs 진행
                dfs(depth + 1)
                result.pop()
                marks[i] += 1


dfs(0)
print(max_ans)
print(min_ans)
