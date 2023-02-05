# 한 줄로 서기 S2
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
q = []

for i in range(n - 1, -1, -1):
    if not q:  # 리스트가 비어있을 때
        q.append(i + 1)
    else:
        if arr[i] == 0:  # 왼쪽에 큰 사람이 없으면 앞에 삽입
            q.insert(0, i + 1)
        else:  # 왼쪽에 큰 사람이 있는 수만큼 뒤로 가서 삽입
            q.insert(arr[i], i + 1)

print(*q)
