# 병든 나이트 S3
import sys

N, M = map(int, sys.stdin.readline().split())

if N == 1:  # 세로가 1 -> 이동 불가
    print(1)
elif N == 2:  # 세로가 2
    print(min(4, (M + 1) // 2))
    # 방문횟수가 5가 되면 4가지 방법 모두 사용
    # 따라서 N==2일 때 방문횟수는 4를 초과할 수 없음
else:
    if M <= 6:
        print(min(4, M))
    else:  # 오른쪽 2칸 이동 두 번 후에 한 칸씩
        print(M - 2)
