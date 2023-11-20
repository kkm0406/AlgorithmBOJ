# 과제는 끝나지 않아! S3

import sys

input = sys.stdin.readline
n = int(input())
st = []
result = 0
for i in range(n):
    task = list(map(int, input().split()))
    if task[0] == 1:
        if task[-1] == 1:
            result += task[1]
        else:
            st.append([task[1], task[2] - 1])
    else:
        if not st:
            continue
        else:
            st[-1][-1] -= 1
            if st[-1][-1] == 0:
                result += st[-1][0]
                st.pop()

print(result)
