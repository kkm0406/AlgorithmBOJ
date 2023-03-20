# 주사위 쌓기 G5
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
# 주사위 아랫면에 따라 윗면이 어떻게 결정되는지 dict에 저장
rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
ans = 0

for i in range(6):  # 첫 번째 주사위를 기준으로 아랫면을 두는 모든 경우 확인
    result = []  # n번째 주사위의 옆면 최댓값을 저장할 리스트
    tmp = [1, 2, 3, 4, 5, 6]  # 1~6번째 면
    tmp.remove(arr[0][i])  # 1~6번째 면 중 하나를 아랫면으로 생각하여 제거
    top = arr[0][rotate[i]]  # dict에 의해 윗면 계산
    tmp.remove(top)  # 윗면도 제거
    result.append(max(tmp))  # 첫번째 주사위 옆면 중 최대값

    for j in range(1, n):  # 두 번째 주사위부터 마지막 주사위까지
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.remove(top)  # 이전 주사위의 아랫면 삭제
        top = arr[j][rotate[arr[j].index(top)]]  # 현재 주사위 윗면 계산
        tmp.remove(top)  # 현재 주사위 윗면 삭제
        result.append(max(tmp))  # 현재 주사위 옆면 중 최대값

    ans = max(ans, sum(result))

print(ans)
