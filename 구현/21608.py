# 상어 초등학교 G5
import sys

input = sys.stdin.readline
n = int(input())
students = [list(map(int, input().split())) for _ in range(n ** 2)]
seat = [[0] * n for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for num in range(n ** 2):
    like_stds = students[num][1:]  # 자리를 정할 학생이 좋아하는 학생
    pos = []  # 현재 학생이 앉을 수 있는 자리 리스트
    for i in range(n):
        for j in range(n):
            if seat[i][j] == 0:  # 해당 좌석이 비어있으면
                like_num, empty_num = 0, 0  # 인접한 칸의 좋아하는 학생 수, 빈 자리수
                for k in range(4):  # 상하좌우 탐색
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] in like_stds:  # 인접한 칸에 좋아하는 학생이 있으면
                            like_num += 1
                        if seat[nx][ny] == 0:  # 인접한 칸이 비어있으면
                            empty_num += 1

                pos.append((like_num, empty_num, i, j))  # 현재 학생이 앉을 수 있는 자리 리스트에 추가

    # 좋아하는 학생수, 빈 자리수는 클수록, 행과 열은 작을수록 조건에 맞춰 정렬
    pos.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    # 학생 앉히기
    seat[pos[0][2]][pos[0][3]] = students[num][0]

result = 0
# 만족도를 쉽게 구하기 위해 오름차순 정렬
students.sort()

for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):  # 현재 위치 기준 상하좌우 탐색
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                # 인접한 칸에 좋아하는 학생이 있으면
                if seat[nx][ny] in students[seat[i][j] - 1]:
                    cnt += 1
        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)
