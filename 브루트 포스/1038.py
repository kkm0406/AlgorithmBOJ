# 감소하는 수 G5
import sys

n = int(sys.stdin.readline())

num = []
ans = []


def check(i):
    global num
    if len(num) == 1:
        return 1
    if num[-2] > i:  # 새로운 추가된 수가 이전의 수보다 작으면
        return 1
    else:
        return 0


def dfs(depth):
    global num
    for i in range(10):  # 첫번째 자리수
        num.append(i)  # 첫번째 자리수 append
        if check(i):  # 새로운 수를 추가했을 때 감소할 수 있으면
            dfs(depth + 1)  # 감소진행
            ans.append(int(''.join(str(x) for x in num)))  # ans에 append(감소하는 수)
        num.pop()


dfs(0)
ans.sort()

if n >= len(ans):  # 감소하는 수 배열의 크기보다 크면
    print(-1)
else:
    print(ans[n])
