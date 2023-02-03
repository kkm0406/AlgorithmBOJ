# 로또 S2
# combination 라이브러리 사용
# dfs - 8 1 2 3 5 8 13 21 34
# s배열에는 1, 2, 3, 5, 8, 13, 21, 34가 담긴다.
# dfs함수를 처음 쓰게 되면
# combi배열에는 차례대로 1, 2, 3, 5, 8, 13이 담기게 된다.
# depth가 6이기때문에 출력을 해주고 return하여 이전 함수로 돌아가게 된다.
# for 문의 i는 증가한 상태이므로 1, 2, 3, 5, 8, 21이 담기게 된다.
# 이런식으로 return하여 이전 함수로 돌아가 숫자를 담게 된다.
import sys
sys.setrecursionlimit(10**6)
combi = [0 for i in range(13)]


def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=" ")
        print()
    for i in range(start, len(arr)):
        combi[depth] = arr[i]
        dfs(i + 1, depth + 1)


while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr == [0]:
        break

    del arr[0]

    dfs(0, 0)
    print()
