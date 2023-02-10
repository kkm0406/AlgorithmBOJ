# 부등호 S1
import sys

input = sys.stdin.readline
k = int(input())
arr = list(map(str, input().split()))
visited = [False] * 10
nums = []
min_ans, max_ans = "", ""


# 연산자 계산
def check(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True


def dfs(depth, s):
    global min_ans, max_ans

    # 문자열 구성완료
    if depth == k + 1:
        if not len(min_ans):  # 최솟값이 없으면
            min_ans = s  # 최솟값으로 추가 (처음 만드는 경우가 최솟값)
        else:  # 그 외의 모든 경우는 최댓값으로 추가
            max_ans = s
        return
    for i in range(10):
        if not visited[i]:
            # 문자열 생성x 또는 계산 가능한 경우
            if depth == 0 or check(s[-1], str(i), arr[depth - 1]):
                visited[i] = True
                dfs(depth + 1, s + str(i))
                visited[i] = False


dfs(0, "")
print(max_ans)
print(min_ans)
