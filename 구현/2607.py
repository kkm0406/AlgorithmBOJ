# 비슷한 단어 S3
import sys

input = sys.stdin.readline
n = int(input())
s = sorted(input().strip())
arr = [sorted(input().strip()) for i in range(n - 1)]
result = 0
for string in arr:
    cnt = 0
    for i in s:
        if i in string:  # 비교대상 단어의 알파벳이 문자에 있으면
            string.remove(i)  # 해당 문자에서 제거
        else:  # 없으면 새로운 알파벳
            cnt += 1
    if len(string) <= 1 and cnt <= 1:  # 처리된 문자열 길이가 1이하 && 새로운 알파벳 개수가 1이하
        result += 1

print(result)
