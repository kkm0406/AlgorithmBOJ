# 십자카드 문제 S3
import sys

input = sys.stdin.readline
arr = list(map(int, input().split()))
card = 9999

# 입력한 카드의 시계수
for i in range(4):
    tmp = ""
    for j in range(i, i + 4):
        tmp += str(arr[j % 4])
    card = min(card, int(tmp))


# 시계수 구하는 함수
def get_num(n):
    num = list(str(n))
    tmp_list = []
    for i in range(4):
        tmp = ""
        for j in range(i, i + 4):
            tmp += str(num[j % 4])
        tmp_list.append(tmp)
    return min(tmp_list)


num_list = set()  # 시계수집합
for n in range(1111, card + 1):  # 1111부터 card까지 완전탐색
    if '0' in str(n):  # 0이 포함되었다면 continue
        continue
    num = get_num(n)
    if num not in num_list:  # 시계수가 집합에 없다면
        num_list.add(num)  # 추가

print(len(num_list))
