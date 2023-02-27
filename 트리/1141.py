# 접두사 S2
import sys

input = sys.stdin.readline
n = int(input())
arr = [str(input().strip()) for i in range(n)]
# 접두사가 되는 단어는 다른 단어보다 길이가 작으므로 길이순 정렬
arr.sort(key=lambda x: len(x))
ans = 0
for i in range(n):
    flag = False
    for j in range(i + 1, n):
        # 현재 단어 이후의 단어들에서
        # 현재 단어가 접두사이면
        if arr[j].find(arr[i]) == 0:
            flag = True
            break
    if not flag:  # 접두사가 아닌경우
        ans += 1

print(ans)
