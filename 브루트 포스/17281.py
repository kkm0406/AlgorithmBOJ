# ⚾ G4
import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
perm = permutations(range(1, 9), 8)  # 1~9번 선수의 순열 생성
ans = 0

for i in perm:
    line_up = list(i[:3]) + [0] + list(i[3:])  # 타순 결정(1번 선수는 4번타자 고정)
    idx, score = 0, 0  # idx번 선수와 해당 타순 때 점수
    for inning in arr:  # 매 이닝마다
        out = 0  # 아웃카운트
        b1, b2, b3 = 0, 0, 0  # 베이스 주자
        while True:  # 아웃==3때까지
            if out == 3:
                break
            if inning[line_up[idx]] == 0:  # 아웃
                out += 1  # 아웃카운트 증가
            elif inning[line_up[idx]] == 1:  # 1루타이면
                score += b3  # 3루 선수 홈인
                b1, b2, b3 = 1, b1, b2  # 베이스 진루
            elif inning[line_up[idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif inning[line_up[idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            else:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0
            idx = (idx + 1) % 9
    if score > ans:
        ans = score

print(ans)
