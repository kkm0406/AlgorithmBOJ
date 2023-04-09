# 카드게임 S3
import sys

input = sys.stdin.readline
arr = []
colors = []  # 입력한 카드 색
numbers = []  # 입력한 번호
color_cnt = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}  # 카드 색깔별 개수
number_cnt = [0] * 10  # 번호 개수
result = 0
for _ in range(5):
    a, b = input().split()
    colors.append(a)
    numbers.append(int(b))
    color_cnt[a] += 1
    number_cnt[int(b)] += 1

colors.sort()
numbers.sort()

if 5 in color_cnt.values():  # 카드 5장이 모두 같은 색
    flag = True
    for i in range(1, 5):  # 숫자 연속 판별
        if numbers[i - 1] + 1 != numbers[i]:
            flag = False
            break
    if flag:  # 1번 조건
        result = max(numbers) + 900
    else:  # 4번 조건
        result = max(numbers) + 600
elif 4 in number_cnt:  # 2번 조건
    result = number_cnt.index(4) + 800
elif 3 in number_cnt and 2 in number_cnt:  # 3번 조건
    result = 700 + number_cnt.index(3) * 10 + number_cnt.index(2)
elif 3 in number_cnt:  # 6번 조건
    result = 400 + number_cnt.index(3)
elif number_cnt.count(2) == 2:  # 7번 조건
    tmp = 0
    tmp_list = []
    for i in range(10):
        if number_cnt[i] == 2:
            tmp_list.append(i)
    result = 300 + tmp_list[1] * 10 + tmp_list[0]
elif 2 in number_cnt:  # 8번 조건
    result = 200 + number_cnt.index(2)
else:
    flag = True
    for i in range(1, 5):  # 숫자 연속 판별
        if numbers[i - 1] + 1 != numbers[i]:
            flag = False
            break
    if flag:  # 5번 조건
        result = max(numbers) + 500
    else:  # 9번 조건
        result = max(numbers) + 100
print(result)
