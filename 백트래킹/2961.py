# 도영이가 만든 맛있는 음식 S2
import sys

input = sys.stdin.readline
n = int(input())
taste = [list(map(int, input().split())) for i in range(n)]
ans = 1e9
sour = 0
bitter = 0
visited = [False] * n
nums = []
idx = 0


def dfs(depth, idx):
    global sour
    global bitter
    global ans
    if 1 <= depth <= n:  # 최소 한개의 재료 사용
        sour = nums[0][0]
        bitter = nums[0][1]
        for i in range(1, len(nums)):
            sour *= nums[i][0]
            bitter += nums[i][1]
        # 연산 후 ans 갱신
        if abs(sour - bitter) < ans:
            ans = abs(sour - bitter)
    for i in range(idx, n):
        if not visited[i]:  # 미방문 인덱스면
            visited[i] = True  # 방문하고
            nums.append(taste[i])  # 재료 추가
            dfs(depth + 1, idx + 1)  # 재귀 호출
            nums.pop()  # 재귀 끝나면 pop
            visited[i] = False  # 미방문 처리


dfs(0, 0)  # 재귀를 통해 재료를 결정
print(ans)
