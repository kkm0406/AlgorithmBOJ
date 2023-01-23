# N-Queen G4
import sys

n = int(sys.stdin.readline())
row = [0] * n
# row[i] = j -> 퀸을 [i, j]위치에 놓음
cnt = 0


def check(x):
    for i in range(x):
        # 이미 놓여진 퀸가 같은 열/대각선 상에 있는지 확인
        # (행끼리의 차 == 열끼리의 차)가 True면 대각선 상
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def nqueen(x):
    global cnt
    if x == n:
        # check()가 참일 때
        # x(depth)가 증가하다 n일 때 탈출
        cnt += 1
        return
    else:
        for i in range(n):
            # 0열부터 n-1열부터 놓을 수 있는 곳 찾기
            row[x] = i
            if check(x):  # 행, 열, 대각선 방향에 퀸 여부 확인
                nqueen(x + 1)


nqueen(0)
print(cnt)
