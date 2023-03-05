# 부동산 다툼 S1
import sys

input = sys.stdin.readline
n, q = map(int, input().split())
arr = [int(input()) for i in range(q)]
visited = [False] * (n + 1)


# 점유된 땅을 지나는지 탐색위해 원하는 땅에서부터 루트까지 거슬러 올라감
def search(node):
    target = node  # 루트까지 가는 경로
    taken = 0  # 점유된 땅의 번호

    while target != 1:  # 루트까지 올라가면서
        if visited[target]:  # 점유된 땅이면
            taken = target  # 번호 초기화
        target //= 2  # 위로 이동

    if taken:  # 루트까지 가면서 점유된 땅이 있으면
        print(taken)  # 해당 번호 출력
    else:
        visited[node] = True  # 원하는 땅 점유가능
        print(0)


for i in arr:
    search(i)
