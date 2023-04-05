# 우리집엔 도서관이 있어 S2
import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
cnt = 0
move = max(arr)  # 옮겨야 하는 책
for i in range(n - 1, -1, -1):  # 뒤에서부터 탐색
    if arr[i] != move:  # 위치에 없으면
        cnt += 1  # 1 증가
    else:  # 옮겨야 하는 책이 위치에 있으면
        move -= 1  # 옮길 책 갱신

print(cnt)
