# 추월 S1
# 나오는 차량들을 처음부터 확인하며 현재 차량의 인덱스(들어간 순서)가
# 뒤에 나오는 차량들의 인덱스보다 큰 경우가 하나라도 존재한다면
# 추월한 것이므로 answer 1증가시키고 다음차량을 확인한다.
import sys

input = sys.stdin.readline
n = int(input())
start = {}
end = []

# 터널에 들어가는 차량을 입력받아 enter 딕셔너리에 {'car': i}로 저장한다.
# (car는 입력받은 차량이름, i는 순서를 나타내는 index)
for i in range(n):
    start[input().strip()] = i

for i in range(n):
    end.append(input().strip())

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if start[end[i]] > start[end[j]]:
            cnt += 1
            break

print(cnt)
