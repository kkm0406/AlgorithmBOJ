# 가장 긴 증가하는 부분 수열 2 G2
import sys
import bisect

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]

for num in arr:
    if num > lis[-1]:  # num이 lis의 마지막 원소보다 크면
        lis.append(num)  # 해당 숫자 추가
    else:  # 아니면
        # bisect_left로 num을 넣어줄 인덱스를 찾고
        idx = bisect.bisect_left(lis, num)
        # 해당 인덱스에 추가
        lis[idx] = num

print(len(lis))
