from bisect import bisect_left, bisect_right  # 이진 탐색 라이브러리

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))  # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환 -> 2
print(bisect_right(a, x))  # 정렬된 순서를 유지바면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환 -> 4

arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]


# 값이 [left_val, right_val]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_val, right_val):
    left_val = bisect_left(a, left_val)
    right_idx = bisect_right(a, right_val)
    return right_idx - left_val


print(count_by_range(a, 4, 4))  # 값이 4인 데이터 개수 출력 -> 2
print(count_by_range(a, -1, 3))  # 값이 [-1, 3] 범위에 있는 데이터 개수 출력 -> 6
