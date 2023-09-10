# 괄호 제거 G5

from itertools import combinations
import sys

input = sys.stdin.readline

s = input().strip()
st = []
index = []
for i in range(len(s)):
    if s[i] == '(':
        st.append(i)
    elif s[i] == ')':
        index.append([st[-1], i])  # ['('의 인덱스, ')'의 인덱스] -> 한 쌍의 인덱스
        st.pop()

# index 쌍의 조합을 구함
combs = []
for i in range(1, len(index) + 1):
    tmp = list(combinations(index, i))
    for j in tmp:
        combs.append(j)

result = []
for comb in combs:  # 조합을 순회하면서
    tmp = list(s)
    for i in comb:  # 해당 조합 내의 () 쌍의 인덱스를 찾고
        for j in i:
            tmp[j] = ""  # 해당 위치를 ""으로 변경
    result.append(''.join(tmp))  # 문자열로 변경

result = list(set(result))  # 중복 제거
result.sort()  # 사전순 정렬
for i in result:
    print(i)
