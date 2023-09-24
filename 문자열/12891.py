# DNA 비밀번호 S2

import sys
from collections import deque

input = sys.stdin.readline

s, p = map(int, input().split())
dna = input().strip()
arr = list(map(int, input().split()))  # A, C, G, T
l, r = 0, p - 1
# 비밀번호에 등장하는 알파벳
cnt = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}
# 맨 처음 비밀번호
string = deque(dna[l:r + 1])
# 알파펫 개수
for i in string:
    cnt[i] += 1
result = 0

while r < s:
    # 포함되어야 할 ACGT의 수와 맞으면 +1
    if cnt['A'] >= arr[0] and cnt['C'] >= arr[1] and cnt['G'] >= arr[2] and cnt['T'] >= arr[3]:
        result += 1

    # 오른쪽으로 한 칸 이동 위해 맨 왼쪽 알파벳 체크
    cnt[dna[l]] -= 1
    l += 1
    r += 1
    if r < s:  # 인덱스 에러 방지
        # 새로 추가한 문자의 알파벳 검사
        cnt[dna[r]] += 1

print(result)
