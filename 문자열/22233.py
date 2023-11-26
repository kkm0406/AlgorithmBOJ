# 가희와 키워드 S2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

keywords = {}
for _ in range(n):
    word = input().strip()
    if word in keywords:
        keywords[word] += 1
    else:
        keywords[word] = 1

sum = sum(keywords.values())
for _ in range(m):
    word = input().strip().split(",")

    for i in word:
        if i in keywords:
            if keywords[i] == 0:
                continue
            else:
                keywords[i] = 0
                sum -= 1
    print(sum)
