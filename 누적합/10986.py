# 나머지 합 G3
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
sum = 0
cnt = [0] * m  # 누적합의 나머지를 저장할 리스트, m개인이유는 m으로 나눈 나머지 값 <= m

# 한번의 누적합을 구할 때 나머지를 따로 뽑아서 저장해두고
# 각 나머지 인덱스에서 2개의 수를 뽑아주면 나머지가 0인 구간을 구할 수 있다.
for i in range(n):
    sum += num[i]
    cnt[sum % m] += 1  # 나머지에 맞게 1증가

result = cnt[0]  # m으로 나누어 떨어지는 구간 수

for i in cnt:
    result += i * (i - 1) // 2  # 나머지가 같은 구간 2개를 뽑는 조합

print(result)
