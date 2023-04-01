# 꿀 따기 G5

n = int(input())
arr = list(map(int, input().split()))
# 벌들이 자신의 위치로 부터 꿀통의 위치까지 순차적으로 사이의 모든 꿀을 더함 -> 누적합
prefix_sum = [arr[0]]
for i in range(1, n):
    prefix_sum.append(prefix_sum[i - 1] + arr[i])
result = 0

# 벌이 최대한 꿀로부터 멀리 떨어져있어야 모으는 꿀의 양이 최대

# 1. 꿀이 맨 왼쪽에 있는 경우
# -> 벌1은 가장 오른쪽, 벌2는 꿀과 벌1 사이
for i in range(1, n - 1):
    # 벌1의 꿀양은 -> 마지막 원소를 제외한 합-벌2가 위치한 i번째 꿀의 양
    # 벌2의 꿀양은 -> i번까지의 꿀의 양
    result = max(result, prefix_sum[n - 2] + prefix_sum[i - 1] - arr[i])

# 2. 꿀이 맨 오른쪽에 있는 경우
# -> 벌1은 가장 왼쪽, 벌2는 꿀과 벌1 사이
for i in range(1, n - 1):
    # 벌1: 가장 왼쪽에 위치하기 때문에 모든 원소의 합-0번째 위치의 꿀의 양-벌2가 위치한 i번째 꿀의 양
    # 벌2: i번째 위치라면 i번째부터 n-1까지의 누적합
    result = max(result, prefix_sum[n - 1] - arr[0] - arr[i] + prefix_sum[n - 1] - prefix_sum[i])

# 3. 꿀이 벌 사이에 있을 때
# -> 벌1, 벌2는 리스트 양 끝에
for i in range(1, n - 1):
    # 꿀이 가운데에 있기 때문에 좌우 끝 원소 제외+꿀통 위치만 한 번 더 더함
    result = max(result, prefix_sum[n - 2] - arr[0] + arr[i])

print(result)
