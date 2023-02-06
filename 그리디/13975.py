# 파일 합치기 3 G4
# 1. 파일들 중에서 제일 작은 두개를 뽑는다.
# 2. 합친다
# 3. 합친걸 다시 파일들에 둔다.
# 우선순위큐를 이용해서 항상 작은 값들이 앞으로 가게 함
import heapq
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    file = []
    for i in arr:
        heapq.heappush(file, i)
    result = 0
    while len(file) > 1:
        a = heapq.heappop(file)
        b = heapq.heappop(file)
        result += a + b
        heapq.heappush(file, a + b)

    print(result)
