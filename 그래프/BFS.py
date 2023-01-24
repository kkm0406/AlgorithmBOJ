from collections import deque

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],  # 0번 노드는 없으므로 패스
    [2, 3, 8],  # 1번 노드와 2, 3, 8번 노드 연결
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9


def bfs(start, visited):
    # 큐 구현을 위해 deque 사용
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        # (가장 먼저 들어온 원소)
        v = queue.popleft()
        print(v, end=" ")
        # 아직 방문하지 않은 인접 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(1, visited)
