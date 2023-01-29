# 행복 유치원 G5
# 키 차이가 최소가 되도록 해야하므로 각 원생사이의 키 차이를 구한다.
# 만약 5명을 3그룹으로 나눈다면 원생사이의 키 차이가 가장 큰 두 원생을 기준으로 나누면 된다.
# 즉, k-1개의 키차이가 빠진 나머지 키차이의 합을 구하면 된다.
# 이때, 최솟값을 구하는 것이므로 키 차이를 구한 ans 리스트를 역순으로 정렬한후
# k-1부터 끝까지의 리스트 총 합을 구하면 된다.
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
height = []
for i in range(1, n):
    height.append(arr[i] - arr[i - 1])

height.sort(reverse=True)  # 키 차이를 내림차순 정렬
print(sum(height[k - 1:]))  # k개이므로 k-1번째부터 더함
