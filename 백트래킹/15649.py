# N과 M(1) S3
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n + 1)
arr = []


def dfs(depth):
    if depth == m + 1:  # arr 출력
        print(*arr)
    for i in range(1, n + 1):
        if not visited[i]:  # 미방문 인덱스면
            visited[i] = True  # 방문처리
            arr.append(i)  # arr에 append
            dfs(depth + 1)  # 재귀 호출
            arr.pop()  # 재귀끝나면 pop
            visited[i] = False  # 미방문 처리


dfs(1)
