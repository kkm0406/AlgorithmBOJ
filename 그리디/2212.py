# 센서 G5
import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
coords = sorted(list(map(int, input().split())))

if n <= k:  # 집중국수 k가 센서수 n과 같거나 크다면, 집중국을 센서 위치에 설치하면 되므로 답은 0이 된다.
    print(0)
else:
    dist = []  # 센서 사이 거리를 저장하는 리스트
    for i in range(n - 1):
        dist.append(coords[i + 1] - coords[i])

    # k개의 집중국을 설치해야하므로 coords에서 k개의 구간이 필요
    # k개 분류를 하려면 분류 기준이 되는 것은 k-1개
    # 센서 사이 거리가 큰 것을 제거하면서 기준 생성
    dist.sort(reverse=True)
    for i in range(k - 1):
        dist.pop(0)

    print(sum(dist))
