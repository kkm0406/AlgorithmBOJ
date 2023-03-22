# 지름길 S1
import sys

input = sys.stdin.readline
n, d = map(int, input().split())
road = [list(map(int, input().split())) for i in range(n)]
dist = [i for i in range(d + 1)]  # 각 인덱스에 i까지의 거리 저장

# 0부터 d까지 반복
for i in range(d + 1):
    # 지름길로 간 거리와 고속도로로 간 거리 비교
    dist[i] = min(dist[i], dist[i - 1] + 1)

    # 지름길을 반복하여 최단 거리 업데이트
    for start, end, short in road:
        # 만약에 i가 start랑 같고, end가 고속도로 길이보다 작으며, 현재까지 온 고속도로 길이랑 지름길이 end로 가는 고속도로 길이보다 짧으면
        # end로 가는 거리 업데이트
        if i == start and end <= d and dist[i] + short < dist[end]:
            dist[end] = dist[i] + short

print(dist[d])
