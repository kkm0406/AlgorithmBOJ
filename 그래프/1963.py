# 소수 경로 G4
import sys
from collections import deque

input = sys.stdin.readline

n = 10000  # 2부터 1,000까지의 모든 수에 대하여 소수 판별
prime = [True for i in range(n + 1)]


def get_prime():
    # 에라스토테네스의 체
    for i in range(2, int(n ** 0.5) + 1):  # n의 제곱근 범위까지 조사
        if prime[i]:  # 소수인 상태에서
            j = 2
            while i * j <= n:  # 소수의 배수 체크
                prime[i * j] = False
                j += 1


def bfs():
    q = deque()
    q.append([a, 0])
    visited = [False] * n
    visited[a] = True

    while q:
        now, cnt = q.popleft()
        if now == b:  # 큐에 방문한 숫자가 b와 같으면 종료
            return cnt

        str_now = str(now)  # 빼낸 값을 문자로 변환

        for i in range(4):  # 각 자리수
            for j in range(10):  # 각 자리수에 0~9 대입하면서 소수인지 확인
                result = int(str_now[:i] + str(j) + str_now[i + 1:])
                # 방문 안한 숫자, 소수이면서 1000 이하면
                if not visited[result] and prime[result] and result >= 1000:
                    visited[result] = True
                    q.append([result, cnt + 1])
    return -1


get_prime()
for _ in range(int(input())):
    a, b = map(int, input().split())
    result = bfs()
    if result == -1:
        print('Impossible')
    else:
        print(result)
