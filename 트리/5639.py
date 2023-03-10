# 이진 검색 트리 G5
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
arr = []
# 입력이 없을때까지 반복하여 입력을 리스트에 추가한다.
while True:
    try:
        arr.append(int(input()))
    except:
        break


def postorder(first, end):
    if first > end:
        return
    mid = end + 1  # 오른쪽 노드가 없을 경우(루트보다 큰 값이 없을 때)

    # 서브트리 탐색
    for i in range(first + 1, end + 1):
        if arr[first] < arr[i]:  # 루트보다 큰 값이면 오른쪽 서브트리로
            mid = i  # 왼쪽 서브트리, 오른쪽 서브트리로 나뉘는 부분을 mid로 설정
            break

    postorder(first + 1, mid - 1)  # 왼쪽 서브트리를 재귀적으로 탐색
    postorder(mid, end)  # 오른쪽 서브트리를 재귀적으로 탐색
    print(arr[first])


postorder(0, len(arr) - 1)
