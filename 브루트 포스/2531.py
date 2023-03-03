# 회전 초밥 S1

import sys
from collections import defaultdict

input = sys.stdin.readline
n, d, k, c = map(int, input().split())
sushi = [int(input()) for i in range(n)]
left, right = 0, k - 1  # 슬라이딩 윈도우 사용
ans = 0
eat = defaultdict(int)  # 딕셔너리를 만드는 dict 클래스의 서브 클래스
# 인자로 주어진 객체의 기본값을 딕셔너리값의 초기값으로 지정가능
# (int) -> 0으로 지정

for i in range(k):
    eat[sushi[i]] += 1  # 먹은 종류는 +1

if c not in eat.keys():  # 먹은 초밥 중 c가 없으면
    eat[c] = 1
else:
    eat[c] += 1
ans = max(ans, len(eat))

# 슬라이딩 윈도우 사용
# 투포인터와 비슷하지만 슬라이딩 윈도우는 정렬의 유무와 상관없이 고정적인 범위를 탐색
while left < n:
    eat[sushi[left]] -= 1  # 윈도우 한 칸 이동위해 가장 왼쪽 접시 제거
    if eat[sushi[left]] == 0:  # 해당 접시가 없다면
        del eat[sushi[left]]  # 딕셔너리에서 제거
    left, right = left + 1, right + 1  # 왼쪽, 오른쪽 인덱스 한 칸 이동
    eat[sushi[right % n]] += 1  # 오른쪽 접시 추가
    ans = max(ans, len(eat))

print(ans)
