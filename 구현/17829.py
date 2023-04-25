# 222-풀링 S2
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


# 분할정복 사용
def pooling(n, x, y):
    size = n // 2
    if n == 2:
        result = sorted([arr[x][y], arr[x + 1][y], arr[x][y + 1], arr[x + 1][y + 1]])
        return result[2]
    left_top = pooling(size, x, y)  # 좌측 상단 구역
    right_top = pooling(size, x, y + size)  # 우측 상단 구역
    left_bottom = pooling(size, x + size, y)  # 좌측 하단
    right_bottom = pooling(size, x + size, y + size)  # 우측 하단
    # 재귀적으로 처리하여 2x2 행렬까지 나눠져 실행한 과정을 반복하게 함
    result = sorted([left_top, left_bottom, right_bottom, right_top])
    return result[2]


# 배열 길이, x, y좌표
ans = pooling(n, 0, 0)
print(ans)
