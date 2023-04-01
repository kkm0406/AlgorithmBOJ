# 숫자 야구 S3
import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())

# 모든 경우의 수 순열 생성
perms = list(permutations(range(1, 10), 3))

for _ in range(n):
    num, s, b = map(int, input().split())
    num = list(str(num))
    idx = 0
    for i in range(len(perms)):
        i -= idx
        cnt_s, cnt_b = 0, 0 #스트라이크 수, 볼 수
        for j in range(3):
            num[j] = int(num[j])
            if num[j] in perms[i]: #입력한 숫자의 j번째 원소가 순열의 i번째 원소에 있으면
                if j == perms[i].index(num[j]): #있는 위치의 인덱스가 같으면
                    cnt_s += 1 #스트라이크
                else:
                    cnt_b += 1 #볼
        if cnt_b != b or cnt_s != s: #스트라이크, 볼 수에 맞지 않으면
            perms.remove(perms[i]) #제거
            idx += 1 #제거했으니

print(len(perms))
