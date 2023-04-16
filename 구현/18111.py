# 마인크래프트 S2
import sys

input = sys.stdin.readline
n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
result = sys.maxsize
height = 0
for h in range(257):  # 0 ~ 256층까지 반복
    use, add = 0, 0  # 인벤토리에서 꺼낸 개수, 추가한 개수
    for i in range(n):
        for j in range(m):
            if arr[i][j] < h:  # 현재 층보다 낮으면
                use += (h - arr[i][j])  # 그만큼 인벤토리에서 꺼냄
            else:
                add += (arr[i][j] - h)  # 그만큼 인벤토리에 추가
    add_cnt = add + b  # 인벤토리에 추가한 개수
    if add_cnt < use:  # 추가한거보다 꺼낸 개수가 많으면
        continue  # continue
    time = 2 * add + use  # 걸린 시간
    if time <= result:
        result = time
        height = h

print(result, height)
