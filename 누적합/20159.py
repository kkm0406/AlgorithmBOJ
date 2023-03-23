# 동작 그만. 밑장 빼기냐? G5
import sys

input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
orgin = sum(card[::2])  # 밑장빼기 없이 진행했을 때 (홀수번째 카드만 뽑음)
j_sum = orgin
result = orgin

# 밑장빼기 진행 시 순서가 바뀜
# 1.정훈이 차례에서 밑장빼기 진행 시
for i in range(n - 1, 0, -2):  # 맨뒤에 카드를 갖게 됨
    j_sum += card[i]  # 밑장빼기한 i번째 카드를 뽑아 더하고
    j_sum -= card[i - 1]  # 기존에 뽑았던 카드 빼기
    result = max(result, j_sum)

# 2. 상대방 차례에서 밑장빼기 -> 밑장 뺀 카드를 상대에게
j_sum = orgin
for i in range(n - 2, 1, -2):
    j_sum -= card[i]  # 뽑았던 카드 빼기
    j_sum += card[i - 1]  # 새로운 카드 뽑아 더하기
    result = max(result, j_sum)

print(result)
