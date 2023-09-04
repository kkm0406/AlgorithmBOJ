# Z S1

import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

cnt = 0


# r, c가 해당하는 사분면을 파악 -> 해당 사분면만 탐색
def check(x, y, size):
    global cnt
    # 해당 좌표가 있는 사분면이 아니면 -> 해당 사분면 전체 칸 수를 더함
    if x > r or x + size <= r or y > c or y + size <= c:
        cnt += size ** 2
        return

    # 해당 사분면에 존재
    if size > 2:
        # 분할 탐색 진행
        size = size // 2
        check(x, y, size)
        check(x, y + size, size)
        check(x + size, y, size)
        check(x + size, y + size, size)
    else:
        # 2 * 2 범위 내에서 탐색
        if r == x and y == c:
            print(cnt)
        elif r == x and y + 1 == c:
            print(cnt + 1)
        elif r == x + 1 and y == c:
            print(cnt + 2)
        else:
            print(cnt + 3)
        sys.exit()


check(0, 0, 2 ** n)
