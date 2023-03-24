# 보석 상자 S1
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for i in range(m)]

# 한 명에게 줄 수 있는 보석의 개수: 1개 ~ 보석 중 최대 보석 개수
start = 1
end = max(arr)
result = end

# 제일 많은 보석 개수 7개씩 나눈다고 하면, 5명에게 각각 7,7,1,4,4를 나눠줘야 한다. 질투심 = 7이며, 보석이 남지 않는다.
# 6개씩 나누면, 7명에게 각각 6,6,1,1,1,4,4를 나눠주므로 질투심 = 6, 보석이 남지 않는다.
# 5개 -> 7명에게 각각 5,5,2,2,1,4,4이므로 질투심 = 5, 남는 보석 0
# 4개 -> 7명에게 각각 4,4,3,3,1,4,4 -> 질투심 = 4, 남는 보석 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0  # 보석을 mid개 만큼 나누었을 때 사람 수
    for i in arr:
        cnt += i // mid
        if i % mid > 0:  # mid로 나누었을 때 나머지가 1이상이면 나머지만큼 한 명에게 추가 지급
            cnt += 1

    # n명보다 많은 인원에게 나누어준 것 -> 더 적게 가져가야함
    if cnt > n:
        start = mid + 1
    else:
        end = mid - 1
        result = min(result, mid)

print(result)
