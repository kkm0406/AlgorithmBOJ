# KCPC S2

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    record = {x: [0, 0, 0] for x in range(1, n + 1)}  # 총점, 제출횟수, 시간
    score = {x: [0] * (k + 1) for x in range(1, n + 1)}  # 문제별 점수

    for k in range(1, m + 1):
        i, j, s = map(int, input().split())
        if score[i][j] < s:  # 문제 최고점 갱신
            score[i][j] = s
            record[i][0] = sum(score[i])
        record[i][1] += 1  # 제출횟수
        record[i][2] = k  # 시간

    # 점수 높은순, 제출횟수 적은순, 제출시간 빠른순
    result = sorted(record.items(), key=lambda x: (x[1][0], -x[1][1], -x[1][2]), reverse=True)
    for i in range(len(result)):
        if result[i][0] == t:
            print(i + 1)
            break
