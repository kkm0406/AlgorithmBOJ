# 차이를 최대로 S2
# permutaion 이용
# 재귀 이용
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
visited = [False] * n
nums = []
result = 0


def check(depth):
    global result
    if depth == n:  # depth==n이면 계산 시작
        s = 0
        for i in range(n - 1):
            s += abs(nums[i] - nums[i + 1])
        if s > result:
            result = s
        return
    for i in range(n):
        if not visited[i]:  # 방문안한 인덱스이면
            visited[i] = True  # 방문처리
            nums.append(arr[i])  # 해당 원소 append
            check(depth + 1)  # 다음 재귀 진행
            nums.pop()  # 재귀끝나면 pop
            visited[i] = False  # 미방문처리


check(0)
print(result)
