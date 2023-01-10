# 숫자 정사각형 S4
import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))

result = []
for i in range(n):
    for j in range(m):
        for k in range(min(n, m)):  # 정사각형 변의 최대 길이는 min(n, m)
            if i + k < n and j + k < m:  # arr index를 넘지 않으면서
                if arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]:
                    # 정사각형 범위내 동일한 값이 있을 때
                    result.append((k + 1) ** 2)

print(max(result))
