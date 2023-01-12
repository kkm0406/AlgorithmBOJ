# 킹 S3
import sys

k, s, n = sys.stdin.readline().split()
arr = [sys.stdin.readline().strip() for i in range(int(n))]
left = ['8', '7', '6', '5', '4', '3', '2', '1']  # 세로
right = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # 가로
dir = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0],
       'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}
# R, L, B, T, RT, LT, RB, LB

kx, ky = left.index(k[1]), right.index(k[0])
sx, sy = left.index(s[1]), right.index(s[0])
for i in arr:
    k_nx, k_ny = kx + dir[i][0], ky + dir[i][1]
    if k_nx == sx and k_ny == sy:  # 왕이 이동할 위치에 돌이 있으면
        s_nx, s_ny = sx + dir[i][0], sy + dir[i][1]
        if 0 <= s_nx < 8 and 0 <= s_ny < 8:  # 체스판 범위에 맞는지 확인
            sx, sy = s_nx, s_ny
            kx, ky = k_nx, k_ny

    else:
        if 0 <= k_nx < 8 and 0 <= k_ny < 8:  # 체스판 범위에 맞는지 확인
            kx, ky = k_nx, k_ny

print(right[ky] + left[kx])
print(right[sy] + left[sx])
