# 졸려 G5

import sys

input = sys.stdin.readline
x = int(input())
word = input().strip()
origin = word
# 변환된 문자열이 들어올 리스트
word_list = [word]


def mix_word():
    global word, word_list
    new_word = ""
    mid = len(word) // 2
    for idx in range(mid):
        # 규칙에 따라 현재 문자열에서 변환
        new_word += word[idx] + word[len(word) - 1 - idx]

    # 문자열의 길이가 홀수이면
    if len(word) % 2 != 0:
        # 문자열의 가운데 문자를 뒤에 추가
        new_word += word[len(word) // 2]

    # 현재 문자 변환
    word = new_word


def solve():
    while True:
        # 문자열 변환
        mix_word()
        # 처음 입력한 문자열과 변환된 문자열이 같아졌으면 break
        if origin == word:
            break
        # 생성된 문자열을 리스트에 추가
        word_list.append(word)
    # 0번째에서 -x번째가 x번 변환된 문자열
    print(word_list[-x % len(word_list)])


solve()
