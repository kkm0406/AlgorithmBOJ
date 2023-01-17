# 한수 S4
import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(1, n + 1):
    if i < 100:
        cnt += 1
    else:
        s = str(i)
        val = int(s[1]) - int(s[0])
        flag = True
        for j in range(2, len(s)):  # 두번째수부터 등차를 확인
            if int(s[j]) - int(s[j - 1]) != val:
                flag = False
                break
        if flag:
            cnt += 1

print(cnt)
