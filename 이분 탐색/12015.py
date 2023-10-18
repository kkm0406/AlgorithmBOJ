# 가장 긴 증가하는 부분 수열 2 G2
import sys
import bisect

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]


def find_place(i):
    left = 0
    right = len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] == i:
            return mid
        elif lis[mid] < i:
            left = mid + 1
        else:
            right = mid - 1
    return right

# for로 A의 요소를 돌면서(item으로 두자),
# item이 LIS의 마지막 원소보다 크면 바로 LIS에 넣어주고,
# 작거나 같으면 findPlace로 item을 넣을 인덱스를 찾고 거기에 넣어준다.
# 이걸 끝까지 반복하면, LIS 리스트는 실제 LIS는 아니지만 "길이" 값 만큼은 조건을 만족
# len(LIS)를 print해준다.
for i in arr:
    if lis[-1] < i:
        lis.append(i)
    else:
        # idx = find_place(i)
        idx = bisect.bisect_left(lis, i)
        lis[idx] = i

print(len(lis))
