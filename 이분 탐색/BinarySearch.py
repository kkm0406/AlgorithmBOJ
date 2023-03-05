# 이진 탐색

n, target = 10, 7
arr = [1, 3, 5, 7, 8, 11, 13, 15, 17, 19]  # 정렬된 리스트


def binary_search(start, end):  # 함수구현
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(start, mid - 1)
    else:
        return binary_search(mid + 1, end)

    # while start <= end:
    #     mid = (start + end) // 2
    #     if arr[mid] == target:
    #         return mid
    #     elif arr[mid] > target:
    #         end = mid - 1
    #     else:
    #         start = mid + 1


result = binary_search(0, n - 1)
print(result + 1) if result is not None else print('no such data')
