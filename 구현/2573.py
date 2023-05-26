# 빙산 G4
# pypy제출

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 3
time = 0


def cnt_water(i, j):
    cnt = 0
    for dx, dy in dir:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                cnt += 1
    return cnt


def bfs(i, j):
    visited[i][j] = True
    q = deque([[i, j]])

    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] > 0:
                visited[nx][ny] = True
                q.append([nx, ny])


while True:
    time += 1

    # 주변에 바다 개수 세기
    water = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                cnt = cnt_water(i, j)
                if cnt > 0:
                    water.append((i, j, cnt))

    # 바다 개수만큼 줄이기
    for x, y, cnt in water:
        tmp = arr[x][y] - cnt
        if tmp >= 0:
            arr[x][y] = tmp
        else:
            arr[x][y] = 0

    # 덩어리 세기
    visited = [[False] * m for i in range(n)]
    area = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                area += 1

    if area >= 2:
        print(time)
        break

    tmp_sum = 0
    for i in arr:
        tmp_sum += sum(i)

    if tmp_sum == 0:
        print(0)
        break

# --------------------------------------------------------------
# C++
# define _CRT_SECURE_NO_WARNINGS
# include <iostream>
# include <vector>
# include <algorithm>
# include <deque>
# using namespace std;
#
# int n, m;
# int dx[4] = {-1, 0, 1, 0};
# int dy[4] = { 0, 1, 0, -1 };
# int time_cnt = 0;
# int arr[300][300] = {};
# int visited[300][300] = {};
#
# int cnt_water(int x, int y) {
# 	int cnt = 0;
# 	for (int i = 0;i < 4;i++) {
# 		int nx = x + dx[i];
# 		int ny = y + dy[i];
# 		if (0 <= nx < n && 0 <= ny < m) {
# 			if (arr[nx][ny] == 0) {
# 				cnt += 1;
# 			}
# 		}
# 	}
# 	return cnt;
# }
#
# void reset_visited() {
# 	for (int i = 0;i < 300;i++) {
# 		for (int j = 0;j < 300;j++) {
# 			visited[i][j] = 0;
# 		}
# 	}
# }
#
# void bfs(int x, int y) {
# 	visited[x][y] = 1;
# 	deque<pair<int, int>> q;
# 	q.push_back(make_pair(x, y));
# 	while (!q.empty()) {
# 		int x = q.back().first;
# 		int y = q.back().second;
# 		q.pop_back();
#
# 		for (int i = 0;i < 4;i++) {
# 			int nx = x + dx[i];
# 			int ny = y + dy[i];
# 			if (0 <= nx < n && 0 <= ny < m && visited[nx][ny] == 0 && arr[nx][ny]>0) {
# 				visited[nx][ny] = 1;
# 				q.push_back(make_pair(nx, ny));
# 			}
# 		}
# 	}
# }
#
# int main() {
# 	scanf("%d %d", &n, &m);
# 	for (int i = 0;i < n;i++) {
# 		for (int j = 0;j < m;j++) {
# 			scanf("%d", &arr[i][j]);
# 		}
# 	}
#
# 	while (true) {
# 		time_cnt += 1;
#
# 		vector < pair<pair<int, int>, int>> water;
# 		for (int i = 0;i < n;i++) {
# 			for (int j = 0;j < m;j++) {
# 				int cnt = cnt_water(i, j);
# 				if (cnt > 0) {
# 					water.push_back(make_pair(
# 						make_pair(i, j), cnt));
# 				}
# 			}
# 		}
#
# 		for (int i = 0;i < water.size();i++) {
# 			int x = water[i].first.first;
# 			int y = water[i].first.second;
# 			int cnt = water[i].second;
# 			int tmp = arr[x][y] - cnt;
# 			if (tmp >= 0) {
# 				arr[x][y] = tmp;
# 			}
# 			else {
# 				arr[x][y] = 0;
# 			}
# 		}
#
# 		reset_visited();
# 		int area = 0;
# 		for (int i = 0;i < n;i++) {
# 			for (int j = 0;j < m;j++) {
# 				if (arr[i][j] > 0 && visited[i][j] == 0) {
# 					bfs(i, j);
# 					area += 1;
# 				}
# 			}
# 		}
#
# 		if (area >= 2) {
# 			printf("%d", time_cnt);
# 			return 0;
# 		}
#
# 		int tmp_sum = 0;
# 		for (int i = 0;i < n;i++) {
# 			for (int j = 0;j < m;j++) {
# 				tmp_sum += arr[i][j];
# 			}
# 		}
#
# 		if (tmp_sum == 0) {
# 			printf("0");
# 			return 0;
# 		}
# 	}
#
# 	return 0;
# }
