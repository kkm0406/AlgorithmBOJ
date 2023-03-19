# 숫자고르기 G5
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
n = int(input())

# 첫째 배열과 둘째 배열사이 사이클 여부를 확인
# 첫째 배열과 같은 인덱스의 둘째 배열이 연결되어 있다고 생각
arr = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    arr[i].append(int(input()))


def dfs(x):
    global result
    if not visited[x]:
        visited[x] = True
        for i in arr[x]:  # 연결된 정점 탐색
            first.add(x)  # 첫째 배열에서 뽑은 숫자
            second.add(i)  # 둘쨰 배열에서 뽑은 숫자
            if first == second:  # 뽑은 집합이 같으면
                result += list(first)  # 결과에 추가
                return
            dfs(i)


result = []
for i in range(1, n + 1):
    first = set()  # 첫째줄에서 고를 숫자
    second = set()  # 둘째줄에서 고를 숫자
    visited = [False] * (n + 1)  # 각 숫자 방문 여부
    dfs(i)

result = list(set(result))
result.sort()
print(len(result))
for i in result:
    print(i)
