# 나무 자르기 S2
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))


def binary_search():
    start = 0  # 0부터 시작
    end = max(tree)  # 가장 긴 나무의 길이
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        h = 0
        for i in tree:
            if i > mid:  # 나무 길이가 자를 나무 길이보다 크면
                h += i - mid
        if h >= m:  # 자른 나무 길이가 m보다 크거나 같으면
            ans = mid
            start = mid + 1
        else:  # 자른 나무 길이가 m보다 작으면
            end = mid - 1
    return ans


print(binary_search())
