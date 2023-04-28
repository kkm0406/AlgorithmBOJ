# 싸이버개강총회 S2
import sys

input = sys.stdin.readline
s, e, q = input().split()
# 입력한 시간에서 :빼고 int로 형변환
s = int(s[:2] + s[3:])
e = int(e[:2] + e[3:])
q = int(q[:2] + q[3:])
arr = set()
cnt = 0
while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= s:  # 시작전에 왔으면
            arr.add(name)  # 입장
        elif e <= time <= q and name in arr:  # 끝나고 스트리밍 끝날때까지, 입장한 사람이면
            arr.remove(name)  # 퇴장
            cnt += 1  # 사람수 +1
    except:
        break
print(cnt)
