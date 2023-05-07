# 트리의 기둥과 가지 G5
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, d = map(int, input().split())
    tree[a].append([b, d])
    tree[b].append([a, d])

visit = [False] * (n + 1)
gigalen = 0  # 기가노드까지 거리
giganode = -1  # 기가노드
ans = 0  # 기가노드부터 리프노드까지 러기
leaf_check = 0  # 기가노드가 없을 때 거리를 저장할 변수


def dfs1(start, count):
    global gigalen, giganode, leaf_check
    tmp = []
    visit[start] = True
    for i, j in tree[start]:
        if not visit[i]:
            tmp.append([i, j])  # 방문안한 지점의 가중치와 위치 저장
            leaf_check += j  # 모든 트리 자식이 1개일수도 있으니 가중치 매번 더해줌

    if len(tmp) >= 2:  # 자식노드가 2개 이상일 때
        gigalen = count  # 루트부터 기가노드까지 거리
        giganode = start  # 기가노드
        return
    else:
        if tmp:
            dfs1(tmp[0][0], count + tmp[0][1])


def dfs2(start, count):
    global ans
    visit[start] = True
    for i, j in tree[start]:
        if not visit[i]:
            ans = max(ans, count + j)  # 기가노드부터 리프노드까지 거리 갱신
            dfs2(i, count + j)


dfs1(r, 0)
dfs2(giganode, 0)

if giganode == -1:
    print(leaf_check, ans)
else:
    print(gigalen, ans)
