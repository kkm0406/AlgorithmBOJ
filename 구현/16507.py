# 어두운 건 무서워 S1
import sys

r, c, q = map(int, sys.stdin.readline().split())
arr = []
points = []
dp = [[0 for i in range(0, c + 1)] for _ in range(r + 1)]
for i in range(r):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 픽섹 밝기의 누적합 저장
for i in range(1, r + 1):
    for j in range(1, c + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + arr[i - 1][j - 1]

for i in range(q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    points.append([x1, y1, x2, y2])

for i in range(len(points)):
    x1, y1, x2, y2 = points[i][0], points[i][1], points[i][2], points[i][3]
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    # 사진 일부분에 해당하는 누적값
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result // area)
