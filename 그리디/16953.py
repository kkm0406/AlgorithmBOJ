# A -> B S2
import sys

a, b = map(str, sys.stdin.readline().split())

flag = True
cnt = 0
while True:
    if b[-1] == '1':  # 1로 끝날 때
        b = b[:-1]
        cnt += 1
    elif int(b[-1]) % 2 == 0:  # 2로 나누어 떨어질 때
        b = str(int(b) // 2)
        cnt += 1
    elif int(b[-1]) % 2 != 0:  # 2로 나누어 떨어지지 않음(한자리)
        if int(b) != int(a):  # (한자지 홀수 일 때 b와 a가 같지 않으면 a->b 불가)
            cnt = -1
            break

    if int(b) < int(a) or b == '':  # 연산 후에 b<a이거나 b가 ''이면 -1출력
        cnt = -1
        break
    if int(b) == int(a):
        cnt += 1
        break

print(cnt)
