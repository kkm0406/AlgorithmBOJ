# 배열 돌리기 1 S1
# 배열을 돌리거나 할 때 중요한 점은 하나의 temp 변수를 만들어주고
# 처음 시작할 때 값을 넣어준 뒤, 배열을 돌리다 보면 비어있는 배열이 생기는데
# 그때 temp변수 안에 저장해두었던 값을 빈 배열에 넣어주면 된다.
# 안에 있는 배열도 돌려줘야 하기 때문인데
# n과 m 중에 작은 값은 2로 나눠준 값 만큼 for문을 돌려서
# 가장자리부터 안에 있는 배열까지 돌려주는 방식으로 구현
import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        tmp = arr[x][y]
        for j in range(i + 1, n - i):
            x = j
            prev_value = arr[x][y]
            arr[x][y] = tmp
            tmp = prev_value

        for j in range(i + 1, m - i):
            y = j
            prev_value = arr[x][y]
            arr[x][y] = tmp
            tmp = prev_value

        for j in range(i + 1, n - i):
            x = n - j - 1
            prev_value = arr[x][y]
            arr[x][y] = tmp
            tmp = prev_value

        for j in range(i + 1, m - i):
            y = m - j - 1
            prev_value = arr[x][y]
            arr[x][y] = tmp
            tmp = prev_value

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
