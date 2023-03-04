# 시간 관리 S1
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

# 마지막 일부터 시작해서 가장 늦게 시작할 수 있는 시간 찾기
# -> 끝나는 시간 기준 정렬
arr.sort(key=lambda x: x[1], reverse=True)

time = arr[0][1] - arr[0][0]  # 맨 마지막 일을 시작하는 시간
for i in range(1, n):
    if time > arr[i][1]:  # 일을 끝낸 시간이 i번째 일을 끝마쳐야 하는 시간보다 크면
        time = arr[i][1]  # 일을 끝낸 시간 갱신
    time -= arr[i][0]  # 수행시간만큼 빼기

# 0시부터 시작해도 못끝낼경우 (time < 0) -> -1 출력
print(time) if time >= 0 else print(-1)
