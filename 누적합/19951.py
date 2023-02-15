# 태상이의 훈련소 생활 S1
# "A번째 칸 부터 B번째 칸 까지 +a를 하세요" 라고 한다면, 새로운 배열에서
# "A번째 칸에 +a를, B + 1번째 칸에 -a"를 한 후에,
# 이 배열에서의 누적합을 구하고, 원본 배열과 합치면 됨

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
h = list(map(int, input().split()))
save = [0] * (n + 1)  # a번째, b번째 칸에 k저장

for i in range(m):
    a, b, k = map(int, input().split())
    # a, b 양 끝에만 k 저장 -> 누적합으로 최종 칸의 높이 구함
    save[a - 1] += k
    save[b] -= k

dp = [0] * (n + 1)
dp[0] = save[0]

for i in range(1, n):
    dp[i] = dp[i - 1] + save[i]  # 누적합으로 수행할 최종 높이

for i in range(n):
    h[i] += dp[i]

print(*h)
