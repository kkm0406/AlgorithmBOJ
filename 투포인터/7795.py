# 먹을 것인가 먹힐 것인가 S3
import sys
from bisect import bisect_right

input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    cnt = 0
    for i in b:
        # bisect_right: 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환
        left = bisect_right(a, i)
        cnt += n - left
    print(cnt)
