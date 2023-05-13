#단어 뒤집기 B5
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    s = s.split()
    for i in s:
        tmp = list(i)
        for j in range(len(tmp)-1, -1, -1):
            print(tmp[j], end="")
        print(end=" ")
    print()