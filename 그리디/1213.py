# 팰린드롬 만들기 S3
import sys

s = sys.stdin.readline().strip()
s = "".join(sorted(list(s)))

dict = {}

# 각 알파벳 개수 카운트
for i in s:
    dict[i] = s.count(i)

# s1에 딕셔너리 순서대로 짝수개씩 해당 알파벳 추가
s1 = ""
for i in dict:
    s1 += i * (dict[i] // 2)
    dict[i] = dict[i] - (dict[i] // 2) * 2

# 처리 결과 개수가 1인 알파벳이 있으면 팰린드롬 가능
# 아니면 팰린드롬 불가능
cnt = 0
c = ""
for i in dict:
    if dict[i] >= 1:
        cnt += 1
        c = i
    if cnt >= 2:
        break

if cnt >= 2:
    print("I'm Sorry Hansoo")
else:
    print(s1 + c + s1[::-1])
