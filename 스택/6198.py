# 옥상 정원 꾸미기 G5

import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
st = []
cnt = 0
for item in arr:
    # 현재 빌딩 높이가 st[-1] 높이보다 크거나 같을때까지
    while st and st[-1] <= item:
        st.pop()
    # 현재 빌딩 추가
    st.append(item)
    # 스택에 존재하는 빌딩 -> 볼 수 있는 빌딩
    cnt += len(st) - 1
print(cnt)
