# NBA 농구 S3
import sys

input = sys.stdin.readline
n = int(input())

cnt = {'1': 0, '2': 0}  # 득점 횟수
score_time = {'1': 0, '2': 0}  # 득점 시간
result = {'1': 0, '2': 0}  # 이기고 있던 시간
prev = 0  # 이전에 이기던 팀
for _ in range(n):
    team, time = input().split()
    m, s = map(int, time.split(":"))
    time = m * 60 + s
    cnt[team] += 1  # 해당 팀에 득점 횟수 + 1

    # 비기고 있었으면
    if prev == 0:
        # 득점한 팀의 시간 최신화
        score_time[team] = time
        # prev 변경
        prev = team
    # 어느 한 팀이 이기고 있다가 동점인 상태
    elif prev != 0 and cnt['1'] == cnt['2']:
        # 이전의 팀이 이기고 있던 시간 최신화
        # 현재 득점 시간 - 해당 팀이 마지막으로 득점한 시간
        result[prev] += time - score_time[prev]
        # 무승부 처리
        prev = 0

# 동점으로 안끝났으면 종료시간에서 빼줌
if prev != 0:
    result[prev] += 60 * 48 - score_time[prev]

print("%02d:%02d" % (result['1'] // 60, result['1'] % 60))
print("%02d:%02d" % (result['2'] // 60, result['2'] % 60))
