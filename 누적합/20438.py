# 출석체크 S2
import sys

input = sys.stdin.readline
n, k, q, m = map(int, input().split())
sleeps = [0] * (n + 3)
attends = [0] * (n + 3)

for i in list(map(int, input().split())):
    sleeps[i] = 1  # 조는 학생 1로 표시
for i in list(map(int, input().split())):
    if sleeps[i]:  # 체크할 학생이 졸고 있으면 continue
        continue
    for j in range(i, n + 3, i):
        if not sleeps[j]:  # 체크할 학생이 졸고 있지 않으면
            attends[j] = 1  # 해당 학생 배수 체크

prefix = [attends[0]]
for i in range(1, n + 3):
    # i번 번호까지 출석한 사람 합 구하기
    prefix.append(prefix[-1] + attends[i])

for _ in range(m):
    s, e = map(int, input().split())
    # e-s+1: 구간 전체 인원
    # prefix: s부터 e까지 출석한 인원
    print(e - s + 1 - (prefix[e] - prefix[s - 1]))
