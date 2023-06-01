# 수 이어 쓰기 2 G5

import sys

input = sys.stdin.readline
n, k = map(int, input().split())

last_num = 0  # 마지막으로 사용된 숫자
num_len = 1  # 현재 자릿수
num_cnt = 9  # 현재 자릿수의 모든 숫자의 개수

# 남은 자릿수가 [현재 자릿수 * 현재 자릿수의 모든 숫자의 개수]보다 크다면
while k > num_len * num_cnt:
    k -= num_len * num_cnt  # 남은 자릿수 업데이트
    last_num += num_cnt  # 마지막으로 사용된 숫자
    num_len += 1  # 현재 자릿수 증가
    num_cnt = num_cnt * 10  # 현재 자릿수의 모든 숫자의 개수 증가

# (마지막으로 사용된 숫자 + 1) + (다음 자릿수에서 남은 숫자의 개수)
last_num = (last_num + 1) + ((k - 1) // num_len)

# 마지막으로 사용된 숫자가 n보다 크면
if last_num > n:
    print(-1)
else:
    # 나머지를 계산하여 마지막으로 사용된 숫자의 몇번째 숫자인지 확인
    print(str(last_num)[(k - 1) % num_len])
