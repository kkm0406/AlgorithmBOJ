# 창고 다각형 S1

import sys

input = sys.stdin.readline

n = int(input())
arr = []
# 가장 높은 지붕과 그 때의 인덱스
max_h, max_idx = 0, 0
h = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    h.append(b)
    max_h = max(max_h, b)

# 가장 높은 지붕의 위치 찾기
arr.sort()
for i in range(n):
    if arr[i][1] == max_h:
        max_idx = i
        break

# 가장 높은 지붕 기준으로 왼쪽, 오른쪽 분리
left = arr[:max_idx + 1]
right = list(reversed(arr[max_idx:]))

# 왼쪽 지붕들은 오름차순, 오른쪽 지붕들은 max_h부터 내림차순
st1, st2 = [], []
for a, b in left:
    if not st1:
        st1.append([a, b])
    else:
        if b >= st1[-1][1]:
            st1.append([a, b])

for a, b in right:
    if not st2:
        st2.append([a, b])
    else:
        if b >= st2[-1][1]:
            st2.append([a, b])

# 면적 구하기: (max_h * 전체 길이)에서 비는 부분을 뺌
size = 0
for i in range(1, len(st1)):
    tmp = (st1[i][0] - st1[i - 1][0]) * (max_h - st1[i - 1][1])
    size += tmp

for i in range(1, len(st2)):
    tmp = (st2[i][0] - st2[i - 1][0]) * (max_h - st2[i - 1][1])
    size += abs(tmp)

print(max_h * (arr[-1][0] - arr[0][0] + 1) - size)
