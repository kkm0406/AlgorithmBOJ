# 기타리스트 S1
import sys

input = sys.stdin.readline
n, s, m = map(int, input().split())
v = list(map(int, input().split()))
# 곡 개수 만큼 최대 볼륨값 길이의 배열을 만들어 풀이
# dp[i][j] = i번째 곡을 j볼륨으로 만들 수 있는지 여부
dp = [[0] * (m + 1) for i in range(n + 1)]

# 처음 시작
dp[0][s] = 1

for i in range(1, n + 1):  # 곡의 개수만큼
    for j in range(m + 1):
        if dp[i - 1][j] == 1:  # 볼륨 조절 가능
            if 0 <= j + v[i - 1] <= m:  # v+p[i] 경우
                dp[i][j + v[i - 1]] = 1
            if 0 <= j - v[i - 1] <= m:  # v-p[i] 경우
                dp[i][j - v[i - 1]] = 1

ans = -1
for i in range(m, -1, -1):  # 최대값 찾기위해 내림차순진행
    if dp[n][i] == 1:  # 최대값 발견시 중단
        ans = i
        break
print(ans)
